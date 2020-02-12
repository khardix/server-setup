# khardix.taskd

[Taskwarrior][] synchronization server setup based on personal distribution.

## Dependencies

-   `khardix.extra-repos`: `taskd` packages are present in `server-ports` COPR.
-   `khardix.firewall`: Interface to the firewall

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: khardix.taskd
```

## License

GNU AGPL version 3 or later.

## Author Information

Jan "Khardix" Staněk -- <khardix@gmail.com>
