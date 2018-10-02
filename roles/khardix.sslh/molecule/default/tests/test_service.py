import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.fixture(scope="module")
def facts(host):
    return host.ansible("setup")["ansible_facts"]


def test_sslh_service_state(host):
    """Enabled as dependency of socket"""

    service = host.service("sslh.service")
    assert service.is_enabled
    assert service.is_running


def test_sslh_socket_listening(host, facts):
    """Enabled and listening"""

    addresses = list(
        filter(
            lambda a: not a.startswith("198.168.")
            and not a.lower().startswith("fe80:"),
            facts["ansible_all_ipv4_addresses"] + facts["ansible_all_ipv6_addresses"],
        )
    )

    assert all(host.socket(f"tcp://{addr}:443").is_listening for addr in addresses)
