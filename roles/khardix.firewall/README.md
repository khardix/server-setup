# khardix.firewall

Base firewall setup using [ufw](https://wiki.ubuntu.com/UncomplicatedFirewall).

After this role finishes, the firewall is enabled on all external (non-loopback)
network interfaces, with only default SSH port (22) open.
Dependent services (roles) are expected to open required ports themselves.

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
