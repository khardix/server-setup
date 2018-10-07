# khardix.sslh – SSLH Protocol multiplexer

This role installs the [SSLH](http://www.rutschle.net/tech/sslh/README.html) protocol multiplexer.
It will listen on all external IP addresses on port 443
and forward traffic to localhost (on standard ports).

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

GNU AGPL version 3 or later
