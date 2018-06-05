import os
from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_epel_connection(host):
    """Verify connection to all enabled repo"""

    enabled = host.run("yum repolist enabled")
    assert "epel" in enabled.stdout

    conn_status = host.run("yum makecache")
    assert conn_status.rc == 0
