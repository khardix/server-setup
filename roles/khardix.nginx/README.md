khardix.nginx
=============

Basic nginx setup, prepared for later addition of http(s) sites.

Role variables
--------------

-   `ssl_access_group`: Additional group for the nginx user.
    Should grant read access to the server's SSL certificates.

-   `ssl_unit_name`: Name of SystemD unit responsible for certificate renewal.
    A drop-in will be installed that will reload nginx after the renewal.

Dependencies
------------

-   `khardix.epel`: Source repository for the nginx packages.
-   `khardix.sslh`: Compatibility with ssh on port 443.
-   `khardix.ssl-server-common`: SSL-compatible setup.

Example Playbook
----------------

    - hosts: servers
      roles:
         - khardix.nginx

License
-------

GNU AGPL version 3 or later.

Author Information
------------------

Jan "Khardix" Staněk -- <khardix@gmail.com>
