import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.fixture(scope="module", autouse=True)
def has_openrc(host):
    """These test should only run if the host services are managed by OpenRC"""

    facts = host.ansible("setup")["ansible_facts"]
    if facts["ansible_service_mgr"] != "openrc":
        pytest.skip("Services not managed by OpenRC")


def test_syslog_is_enabled_and_running(host):
    """The syslog service is enabled and running"""

    syslog = host.service("syslog")

    assert syslog.is_enabled and syslog.is_running
