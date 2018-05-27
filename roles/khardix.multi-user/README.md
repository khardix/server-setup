# khardix.multi-user -- Multi-user access to the system

This role ensures the presence of requested users on the target system and their ability to log into it.

## Role Variables

-   `active_users`: List of user descriptions. The recognized fields are:
    -   `name`: User name. **Required**
    -   `ssh_key`: Public SSH key to use for user login. **Required**
    -   `admin`: If true, enable `sudo(1)` for this user.
    -   `password_hash`: `crypt(3)`-compatible hash of the user's password to be set.
        Please note that this role forbids password login with SSH, so this password is used only for `sudo(1)` and similar commands.
    -   `shell`: Name of the login shell. Defaults to bash.

## Dependencies

-   `khardix.hardened-ssh`

## Example Playbook

    - hosts: servers
      roles:
        - khardix.multi-user
      vars:
        active_users:
          - name: khardix
            ssh_key: ...
            admin: yes
            password_hash: ...
            shell: zsh

## License

MIT
