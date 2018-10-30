import os

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize(
    "path,user",
    [
        ("/etc/pki/https/dhparam.pem", "nginx"),
        ("/etc/pki/https/bootstrap.template", "root"),
    ],
)
def test_ssl_basics_accessible(host, path, user):
    """Basics files for TLS setup are accessible by dedicated users"""

    assert host.file(path).exists

    with host.sudo(user):
        host.run_expect({0}, f"test -r {path}")
