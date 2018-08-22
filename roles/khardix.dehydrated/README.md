# khardix.dehydrated

Automatic SSL/TLS certificate requesting and renewal
using the Let's Encrypt CA and dehydrated client.

## Role Variables

-   `dehydrated_user`: Name of the user dedicated to running the client
    (default: `dehydrated`).

-   `ssl_access_group`: Main group of the `dehydrated_user`,
    will get read access to certificates and private keys
    (uses default from `khardix.ssl-server-common`).

-   `ssl_unit_name`: Name (without extension) of the dehydrated service/timer
    which manages the automatic certificate renewal requests
    (uses default from `khardix.ssl-server-common`).

-   `letsencrypt_contact_email`: Contact email for communication with the CA,
    will receive expiration notices (no default, **recommended**).

-   `letsencrypt_api_url`: The URL to direct all certificate requests to;
    useful for testing (default: Live Let's Encrypt API endpoint).

## Dependencies

-   `khardix.epel`: The dehydrated is packaged in EPEL.
-   `khardix.ssl-server-common`: Common setup for SSL management.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: khardix.dehydrated
      ssl_access_group: dehydrated
      letsencrypt_api_url: 'https://acme-staging-v02.api.letsencrypt.org/directory'
      letsencrypt_contact_email: 'khardix@gmail.com'
```

## License

GNU AGPL version 3 or later.

## Author Information

Jan "Khardix" Staněk -- <khardix@gmail.com>
