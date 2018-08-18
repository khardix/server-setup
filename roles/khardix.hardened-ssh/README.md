# khardix.hardened-ssh -- Safer SSHD configuration for public server

This role adjusts the SSH daemon configuration to more hardened values:

-   No root login by default.
-   Listen only on link-local interfaces (uses SSHL for public access).

## Dependencies

-   `khardix.sslh-service`

## Role variables

-   `ssh_root_key` -- Public SSH key of the root. When provided, root is allowed to log in without password.

## Example Playbook

    - hosts: servers
      roles:
         - name: khardix.hardened-ssh
           ssh_root_key: abcdef...

## License

MIT
