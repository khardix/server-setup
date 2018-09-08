import os

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_taskd_running(host):
    """Taskd service is enabled and running"""

    taskd = host.service("taskd.service")

    assert taskd.is_running
    assert taskd.is_enabled
