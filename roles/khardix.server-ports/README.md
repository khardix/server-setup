# khardix.server-ports

A custom [COPR][] repository with software either missing or too old in EPEL.

[COPR]: https://copr.fedorainfracloud.org

## Role Variables

-   `server_ports_project`: `group/name` identification of the [COPR][] project.
    *Default:* `jstanek/server-ports`.

## Dependencies

-   `khardix.epel` -- Package dependencies.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: khardix.server-ports
```

## License

GNU AGPL version 3 or later.

## Author Information

Jan "Khardix" Staněk -- <khardix@gmail.com>
