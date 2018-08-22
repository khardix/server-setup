# khardix.ssl-server-common

This role provides base environment for SSL/TLS server services.
It's intended use is to be a shared dependency for other roles that provide or utilize SSL/TLS functionality.

The role provides the following:

1.  User group that will get read access to the server certificates and private keys.

2.  Rudimentary notification "protocol" that allows services to react to certificate generation and/or renewal.
    This "protocol" has the form of SystemD override directory for the service responsible for certificate management.
    Any service that wishes to react to the certificate renewal should drop an appropriate unit file snippet into this directory.

    *Note:* The actual service (and presumably, timer) is not managed by this role -- only the override directory is.

3.  Facts for easy access to aforementioned values in dependent roles, namely:

    -   `ssl_unit_path`: Full path to the expected certificate renewal service unit file *without extension*.
    -   `ssl_service_dir`: Full path to the "protocol" service override directory.

## Role Variables

-   `ssl_access_group`: Name of the user group with read access to the certificates and keys (default: `ssl`).
-   `ssl_unit_name`: Expected name of the certificate refresh service, without any file extension (default: `ssl-cert-refresh`).

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: khardix.ssl-server-common
      ssl_access_group: https
      ssl_unit_name: certbot
```

## License

GNU AGPL version 3 or later.

## Author information

Jan "Khardix" Staněk -- <khardix@gmail.com>
