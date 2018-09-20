import os

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_ufw_service_enabled(host):
    """UFW service is enabled and running"""

    service = host.service("ufw.service")
    assert service.is_enabled
    assert service.is_running

    with host.sudo():
        status = host.command("ufw status").stdout.strip()
    assert "inactive" not in status


@pytest.mark.parametrize(
    "port,should_be_opened", [(22, True), (80, False), (443, False)]
)
def test_port_status(host, port, should_be_opened):
    """Ensure that key ports are in expected state."""

    with host.sudo():
        open_services = host.command("ufw status").stdout.splitlines()

    opened = any(line.startswith(format(port, "d")) for line in open_services)
    assert opened == should_be_opened
