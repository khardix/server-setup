import os
import shlex

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")

SERVER_PORTS_COPR = "copr:copr.fedorainfracloud.org:jstanek:server-ports"


def test_repository_enabled(host):
    command = ["yum", "-q", "repo-pkgs", SERVER_PORTS_COPR, "list"]

    with host.sudo():
        result = host.run(" ".join(map(shlex.quote, command)))

    assert result.rc == 0, result.stderr
    assert len(result.stdout) != 0
