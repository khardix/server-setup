# khardix.https

Base setup of nginx as modular webserver, with TLS automation via letsencrypt.

## Role variables

-   `letsencrypt_contact_email`: Contact e-mail for CA communication,
    will receive expiration notifications (no default, **recommended**).

-   `letsencrypt_api_url`: The URL fo CA API endpoint for certificate requests
    (default: Live Let's Encrypt API endpoint).

-   `dehydrated_user`: User/group name for privilege dropping (default: `dehydrated`).

## Dependencies

-   `khardix.epel`: Repository for most of the used packages.
-   `khardix.sslh`: Nginx is configured to share port 443.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: khardix.https
```

## License

GNU AGPL version 3 or later.

## Author Information

Jan "Khardix" Staněk -- <khardix@gmail.com>
