import os
import shlex
from types import MappingProxyType

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("redhat")

YUM = ("yum", "-q")

# Package name -> repository name
REPOSITORY_PACKAGE_MAP = MappingProxyType({"epel-release": "epel"})
# Installed COPRs
COPR_LIST = ["copr:copr.fedorainfracloud.org:jstanek:server-ports"]


def run_safe(host, command):
    """Run command with quoted words"""

    return host.run(" ".join(map(shlex.quote, command)))


@pytest.mark.parametrize("package,repo", REPOSITORY_PACKAGE_MAP.items())
def test_repo_from_rpm_is_enabled(host, package, repo):
    """A repository installed from RPM package is enabled"""

    list_installed = YUM + ("list", "installed", package)
    installed = run_safe(host, list_installed)
    assert installed.rc == 0 and package in installed.stdout, installed.stderr

    list_enabled = YUM + ("repolist", "enabled", repo)
    enabled = run_safe(host, list_enabled)
    assert enabled.rc == 0 and repo in enabled.stdout, enabled.stderr


@pytest.mark.parametrize("copr", COPR_LIST)
def test_copr_is_enabled(host, copr):
    """A COPR repository is enabled"""

    list_enabled = YUM + ("repolist", "enabled", copr)
    enabled = run_safe(host, list_enabled)
    assert enabled.rc == 0 and copr in enabled.stdout, enabled.stderr
