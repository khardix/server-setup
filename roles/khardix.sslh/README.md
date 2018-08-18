# khardix.sslh – SSLH Protocol multiplexer

This role installs the [SSLH](http://www.rutschle.net/tech/sslh/README.html) protocol multiplexer.
By default, this will listen on all non-localhost interface ports 443 and forward any traffic to localhost:443.
In order to add another kind of forwarding, use `khardix.sslh-service` role with appropriate parameters.

## Requirements

-   System managed by systemd

Also, the playbook should handle the change of SSH port during execution.

## Dependencies

-   `khardix.epel` -- Enable repository with the `sslh` package.

## Example Playbook

```yaml
- hosts: servers
  pre_tasks:
    - include: detect_used_ssh_port
  roles:
    - role: khardix.sslh
```

## License

MIT
