# khardix.https

Base setup of nginx as modular webserver, with TLS automation via letsencrypt.

## Role variables

-   `letsencrypt_contact_email`: Contact e-mail for CA communication,
    will receive expiration notifications (default: `admin@{{ ansible_fqdn }}`).

-   `letsencrypt_use_live`: Easy toggle between official live and staging
    API endpoints (default: false).

-   `letsencrypt_api_url`: The URL fo CA API endpoint for certificate requests
    (obeys `letsencrypt_use_live` by default).

-   `dehydrated_user`: User/group name for privilege dropping (default: `dehydrated`).

-   `dehydrated_run_request`: Actually request certificates as configured (default: false).

## Dependencies

-   `khardix.epel`: Repository for most of the used packages.
-   `khardix.sslh`: Nginx is configured to share port 443.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: khardix.https
      letsencrypt_use_live: true
      letsencrypt_contact_email: 'khardix@gmail.com'
```

## License

GNU AGPL version 3 or later.

## Author Information

Jan "Khardix" Staněk -- <khardix@gmail.com>
