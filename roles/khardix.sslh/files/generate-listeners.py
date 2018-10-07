#!/usr/bin/env python3
"""Generate SSLH listen directives for all external IP addresses.

External requirements: `ip` utility
"""

import sys
import logging
from argparse import ArgumentParser, FileType
from itertools import chain, product, starmap
from ipaddress import ip_interface
from subprocess import check_output
from textwrap import indent


class ListenSnippet:
    """Container for the 'listen' directive of SSLH configuration."""

    def __init__(self, address_list=None, port_list=None):
        self.address_list = address_list or []
        self.port_list = port_list or []

    def __str__(self):
        """Convert to properly formatted configuration directive."""

        def addr_format(address):
            fmt = "[{}]" if address.version > 4 else "{}"
            return fmt.format(address)

        def instance_format(address, port):
            return '{{ host: "{address}"; port: "{port}"; }}'.format_map(locals())

        addr_iter = map(addr_format, self.address_list)
        port_iter = map(str, self.port_list)
        inst_iter = starmap(instance_format, product(addr_iter, port_iter))

        instance_string = indent(",\n".join(inst_iter), prefix=" " * 4)
        return "listen:\n(\n{}\n);".format(instance_string)


def list_external_addresses():
    """List non-noopback addresses using the `ip` utility."""

    COMMAND = "ip -brief address show"

    ip_output = check_output(COMMAND.split(), universal_newlines=True)
    addr_iter = chain.from_iterable(
        line.strip().split()[2:] for line in ip_output.splitlines()
    )
    iface_iter = map(ip_interface, addr_iter)

    return [iface.ip for iface in iface_iter if not iface.ip.is_loopback]


def main(out):
    """Bind SSLH to all external (not link-local) addresses on port 443"""

    address_list = list_external_addresses()
    external_iter = filter(lambda a: not a.is_link_local, address_list)

    snippet = ListenSnippet(address_list=list(external_iter), port_list=[443])
    logging.info("Writing output into '%s'", out.name)
    print(snippet, file=out)


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        "-o",
        type=FileType("w", encoding="utf-8"),
        default=sys.stdout,
        help="Output file [default: stdout].",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        default=False,
        help="Increase verbosity of output",
    )

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARN)

    main(out=args.output)
