import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_host = AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_nginx_enabled(host):
    """Nginx is enabled and running"""

    nginx = host.service("nginx.service")

    assert nginx.is_running
    assert nginx.is_enabled


@pytest.mark.parametrize("port", [80, 443])
def test_default_server_closes_connection(host, port):
    """There should be no response on request to default server"""

    request = "curl 'http://localhost:{port}'".format(port=port)
    response = host.run(request)

    assert response.rc != 0
    assert "Empty reply from server" in response.stderr


@pytest.mark.parametrize("target", ["80", "127.0.0.1:443", "::1:443"])
def test_nginx_listens(host, target):
    """Nginx listens on expected address/port combination"""

    socket = host.socket("tcp://{target}".format(target=target))
    assert socket.is_listening
