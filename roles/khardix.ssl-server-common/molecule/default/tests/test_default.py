import os

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_ssl_access_group(host):
    """The user access group exists."""

    assert host.group("test-access-group").exists


def test_ssl_protocol_dir_exists(host):
    """The refresh service override directory exists."""

    ssl_unit_name = "test-ssl-unit"
    expected_basename = ".".join((ssl_unit_name, "service", "d"))
    expected_path = os.path.join("/etc/systemd/system", expected_basename)

    assert host.file(expected_path).is_directory
