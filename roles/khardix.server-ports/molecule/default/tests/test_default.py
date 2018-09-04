import os

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_repository_enabled(host):
    with host.sudo():
        result = host.run("yum -q repo-pkgs jstanek-server-ports list")

    assert result.rc == 0
    assert len(result.stdout) != 0
