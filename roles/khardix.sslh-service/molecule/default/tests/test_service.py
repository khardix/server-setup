import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_sslh_service_state(host):
    """Enabled as dependency of socket"""

    assert host.service("sslh.service").is_enabled


def test_sslh_socket_state(host):
    """Enabled and listening"""

    socket = host.service("sslh.socket")
    assert socket.is_enabled
    assert socket.is_running
