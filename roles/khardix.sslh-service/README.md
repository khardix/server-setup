# khardix.sslh-service – Additional SSLH service installations

This role extends the `khardix.sslh` role.
It manages the configuration snippets responsible for multiplexing the various protocols.

## Role Variables

-   `sslh_service` -- Name of the service to demultiplex, i.e. `ssh`, `ssl`.
    See `sslh(8)` for valid values.
-   `sslh_port` -- `localhost` port the service daemon is listening at.

## Dependencies

-   `khardix.sslh`: The main configuration manager.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: khardix.sslh-service  # pulls khardix.sslh automatically
      sslh_service: ssl
      sslh_port: 443
    - role: khardix.sslh-service
      sslh_service: ssh
      sslh_port: 22
```

## License

GNU AGPL version 3 or later

## Author Information

Jan "Khardix" Staněk -- <khardix@gmail.com>
