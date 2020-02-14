import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

ETCHOSTS_PATTERN = re.compile(r"(?P<ip>[0-9a-f.:]+)\s+(?P<fqdn>\S+)")


def test_non_localhost_ip_in_etc_hosts(host):
    """There is at least 1 non-localhost line for `host` in /etc/hosts."""

    FQDN = host.check_output("hostname -f")

    hosts_lines = host.file("/etc/hosts").content_string.splitlines()
    hosts_entry_iter = filter(None, map(ETCHOSTS_PATTERN.match, hosts_lines))

    refers_to_localhost = filter(lambda match: match["fqdn"] == FQDN, hosts_entry_iter)
    non_loopback = filter(
        lambda match: match["ip"] not in {"127.0.0.1", "::1"}, refers_to_localhost
    )

    assert list(non_loopback)
