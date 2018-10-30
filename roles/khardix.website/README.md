# khardix.website

Simple, HTTPS-enabled static web site.

Also serves as base for other, more complicated hosting solutions.

## Role Variables

-   `website_hostname_list`: List of accepted host names for this website.
    The first one is considered to be canonical, others are considered aliases.
    **Mandatory.**

-   `website_owner`: The local user with write access to website's data.
    Default: root.

See also [khardix.https](../khardix.https/README.md) variables.

## Dependencies

-   `khardix.https`: Basis for the website configuration.

## Example Playbook

```yaml
- hosts: servers
  pre_tasks:
    - user: name=khardix
  roles:
    - role: khardix.website
      website_hostname_list: [khardix.cz, www.khardix.cz]
      website_owner: khardix
```

## License

GNU AGPL version 3 or later.

## Author Information

Jan "Khardix" Staněk -- <khardix@gmail.com>
