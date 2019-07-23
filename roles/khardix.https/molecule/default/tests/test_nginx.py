import os
from itertools import chain
from operator import itemgetter

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.fixture(scope="module")
def address_pool(host):
    """Enumerate all existing addresses on host"""

    facts = host.ansible("setup")["ansible_facts"]

    # Extract loopback addresses
    loopback = chain(
        [facts["ansible_lo"].get("ipv4", {}).get("address", None)],
        map(itemgetter("address"), facts["ansible_lo"].get("ipv6", [])),
    )

    # Append external addresses
    addresses = chain(
        filter(None, loopback),
        facts.get("ansible_all_ipv4_addresses", []),
        facts.get("ansible_all_ipv6_addresses", []),
    )

    return set(addresses)


@pytest.fixture(params=["80", "127.0.0.1:443", "::1:443"])
def expected_socket(request, address_pool):
    """Enumerate sockets nginx is expected to listen on"""

    addr, __, port = request.param.rpartition(":")

    if not addr or addr in address_pool:
        return request.param
    else:
        pytest.skip("{addr} is not assigned to host".format(addr=addr))


def test_nginx_enabled(host):
    """Nginx is enabled and running"""

    nginx = host.service("nginx.service")

    assert nginx.is_running
    assert nginx.is_enabled


@pytest.mark.parametrize("protocol", ["http", "https"])
def test_default_server_closes_connection(host, protocol):
    """There should be no response (apart from SSL) on request to default server"""

    request = "curl --insecure '{protocol}://localhost'".format(protocol=protocol)
    response = host.run(request)

    assert response.rc != 0
    assert "Empty reply from server" in response.stderr


def test_nginx_listens(host, expected_socket):
    """Nginx listens on expected socket."""

    description = "tcp://{}".format(expected_socket)
    assert host.socket(description).is_listening


def test_perl_extensions_pass_tests(host):
    """Installed perl extentions pass installed tests"""

    test_script = [
        "cd /usr/share/nginx/perl",
        "for t in t/*.t",
        "do perl -Ilib $t || exit $?",
        "done",
    ]

    results = host.run(";".join(test_script))
    assert results.rc == 0
