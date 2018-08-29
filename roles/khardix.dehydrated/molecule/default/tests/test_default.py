import os

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_dehydrated_configuration(host):
    """dehydrated configuration exists and contains expected values"""

    expected = {"CONTACT_EMAIL": "khardix@gmail.com", "CA": "staging"}

    config = host.file("/etc/dehydrated/config")

    assert config.is_file
    assert config.group == "ssl"
    assert config.mode == 0o640

    for line in config.content_string.splitlines():
        key, __, value = line.partition("=")

        if key not in expected:
            continue

        assert expected[key] in value
        del expected[key]

    assert len(expected) == 0


def test_refresh_timer_is_active(host):
    """The refresh timer is active (waiting) and enabled"""

    timer = host.service("dehydrated.timer")

    assert timer.is_enabled and timer.is_running
