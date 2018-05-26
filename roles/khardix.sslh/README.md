# khardix.sslh – SSLH Protocol multiplexer

This role installs the [SSLH](http://www.rutschle.net/tech/sslh/README.html) protocol multiplexer, and hides SSH behind the 443 port.

## Dependencies

-   `khardix.epel` -- Enable repository with the `sslh` package.

## Requirements

-   System managed by systemd

Also, the playbook should handle the change of SSH port during execution.

## Role variables

-   `sslh_service` -- Name of the service to demultiplex, i.e. `ssh`, `ssl`.
    See `sslh(8)` for valid values.
-   `sslh_port` -- `localhost` port the service daemon is listening at.

## Example Playbook

```yaml
- hosts: servers
  pre_tasks:
    - include: detect_used_ssh_port
  roles:
    - name: khardix.sslh
      sslh_service: ssl
      sslh_port: 443
    - name: khardix.sslh
      sslh_service: ssh
      sslh_port: 22
```

## License

MIT
