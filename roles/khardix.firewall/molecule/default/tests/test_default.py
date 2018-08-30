import os

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize(
    "service,should_be_opened", [("ssh", True), ("http", False), ("https", False)]
)
def test_port_status(host, service, should_be_opened):
    """Ensure that key ports are in expected state."""

    open_services = host.command("firewall-cmd --list-services").stdout.split()

    if should_be_opened:
        assert service in open_services
    else:
        assert service not in open_services


def test_all_interfaces_bound_to_zone(host):
    """All host interfaces are bound to external zone"""

    interfaces = host.ansible("setup")["ansible_facts"]["ansible_interfaces"]
    interfaces = filter(lambda iface: iface != "lo", interfaces)

    for iface in interfaces:
        zone = host.command(f"firewall-cmd --get-zone-of-interface={iface}")
        assert zone.stdout.strip() == "external" or zone.stderr.strip() == "no zone"
