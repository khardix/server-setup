import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("alpine")

# Added tagged repositories
EXTRA_REPOSITORY_LIST = ["testing"]


@pytest.mark.parametrize("repo_tag", EXTRA_REPOSITORY_LIST)
def test_repo_from_rpm_is_enabled(host, repo_tag):
    """A repository with repo_tag is configured."""

    repositories = host.file("/etc/apk/repositories")
    assert repositories.contains(f"@{repo_tag}"), repositories.content_string
