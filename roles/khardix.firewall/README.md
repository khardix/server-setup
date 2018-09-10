# khardix.firewall

Base firewall setup using [firewalld](https://firewalld.org/).

After this role finishes, the firewall is enabled on all external (non-loopback)
network interfaces, with only default SSH port (22) open.
Dependent services (roles) are expected to open required ports themselves.

## Role Variables

-   `firewalld_zone`: Which zone should the configuration be based upon.
    Defaults to `external`.

-   `firewalld_disable_dbus`: Switch SystemD unit type to `simple` from `dbus`.
    Defaults to `false`, but should automatically switched to true
    when the target machine does not support dbus.
    Currently, this applies only to OpenVZ guests.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: khardix.firewall
```

## License

GNU AGPL version 3 or later.

## Author Information

Jan "Khardix" Staněk -- <khardix@gmail.com>
