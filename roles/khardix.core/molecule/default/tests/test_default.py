"""Role testing files using testinfra."""

import pytest


@pytest.fixture
def hosts(host):
    """Contents of /etc/hosts file."""

    return host.file("/etc/hosts").content_string


@pytest.fixture
def fqdn(host):
    """FQDN as reported by the host."""

    return host.check_output("hostname -f")


def test_localhost_in_hosts(hosts):
    """localhost entries are present in /etc/hosts"""

    LOCALHOST_FQDN = " localhost.localdomain "

    matching = [line for line in hosts.splitlines() if LOCALHOST_FQDN in line]
    assert len(matching) == 2
    assert any(line.startswith("127.0.0.1") for line in matching)
    assert any(line.startswith("::1") for line in matching)


def test_fqdn_in_hosts(hosts, fqdn):
    """FQDN entries are present in /etc/hosts"""

    assert any(f" {fqdn} " in line for line in hosts.splitlines())
