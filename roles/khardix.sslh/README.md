# khardix.sslh – SSLH Protocol multiplexer

This role installs the [SSLH](http://www.rutschle.net/tech/sslh/README.html) protocol multiplexer, and hides SSH behind the 443 port.

## Requirements

-   System managed by systemd
-   SSH already installed and running on the target

Also, the playbook should handle the change of SSH port during execution.

## Role variables

-   `services`: Dictionary of services to forward the requests to.
    Keys are protocol names (i.e. `ssl`, `ssh`), values are localhost ports to forward to.
    See `sslh(8)` for available protocol names.

    Defaults: `ssh: 22`, `ssl: 443`

## Example Playbook

```yaml
- hosts: servers
  pre_tasks:
    - include: detect_used_ssh_port
  roles:
    - name: khardix.sslh
      services:
        ssh: 22
        anyprot: 443
```

## License

MIT
