import os
import re
from collections import Counter

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

ETCHOSTS_PATTERN = re.compile(r"(?P<ip>[0-9a-f.:]+)\s+(?P<fqdn>\S+)")


@pytest.fixture
def etchosts(host):
    """Non-empty, non-comment lines from the /etc/hosts file"""

    line_seq = host.file("/etc/hosts").content_string.splitlines()
    line_seq = (line for line in line_seq if line.strip())
    line_seq = (line for line in line_seq if not line.lstrip().startswith("#"))
    return list(line_seq)


def test_non_localhost_ip_in_etc_hosts(host, etchosts):
    """There is at least 1 non-localhost line for `host` in /etc/hosts."""

    FQDN = host.check_output("hostname -f")

    hosts_entry_iter = filter(None, map(ETCHOSTS_PATTERN.match, etchosts))

    refers_to_localhost = filter(lambda match: match["fqdn"] == FQDN, hosts_entry_iter)
    non_loopback = filter(
        lambda match: match["ip"] not in {"127.0.0.1", "::1"}, refers_to_localhost
    )

    assert list(non_loopback)


def test_no_duplicates_in_etc_hosts(host, etchosts):
    """No IP is mentioned twice in /etc/hosts"""

    addr_seq = (line.split(maxsplit=1)[0] for line in etchosts)
    counter = Counter(addr_seq)

    assert all(count == 1 for addr, count in counter.items()), counter
