import os
import random
from pathlib import PosixPath as Path
from stat import S_IRWXU
from string import ascii_letters

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


ROOT_DIR = Path("/srv/http/example.com/")


@pytest.fixture(scope="module")
def index_file(host):
    """Create index file with known content."""

    content = ":".join(random.choices(ascii_letters, k=8))
    target = ROOT_DIR / "en" / "index.html"
    command = f"mkdir -p '{target.parent}' && echo '{content}' >'{target}' && chmod 0644 '{target}'"

    host.run_expect({0}, command)

    return content


@pytest.fixture()
def curl():
    """Base curl command with additional options"""

    return [
        "curl",
        "--insecure",
        "--resolve example.com:80:127.0.0.1",
        "--resolve example.com:443:127.0.0.1",
    ]


def test_root_is_accessible(host):
    """Root directory is writable by expected owner"""

    root = host.file(f"{ROOT_DIR}")

    assert root.is_directory
    assert root.user == "example_user"
    assert root.mode & S_IRWXU == S_IRWXU


def test_server_redirects_to_expected_subdir(host, curl):
    """Server automatically redirect from root"""

    command = curl + ["--head", "https://example.com/"]
    result = host.run(" ".join(command))

    assert result.rc == 0

    response = result.stdout.strip().splitlines()
    assert "303" in response[0]  # HTTP_SEE_OTHER
    assert "Location: /en/" in response[1:]  # redirect


def test_server_serves_content(host, curl, index_file):
    """Server serves expected content"""

    command = curl + ["--location", "http://example.com/en/"]
    result = host.run(" ".join(command))

    assert result.rc == 0
    assert result.stdout.strip() == index_file
