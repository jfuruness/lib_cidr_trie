from ipaddress import IPv4Network, IPv6Network
from typing import Optional


class CIDRNode:
    def __init__(
        self,
        prefix: IPv4Network | IPv6Network | None = None,
        left: Optional["CIDRNode"] = None,
        right: Optional["CIDRNode"] = None,
    ) -> None:
        """Left is 0. Right is 1. Node in CIDR tree"""

        self.prefix: IPv4Network | IPv6Network | None = prefix
        self.left: CIDRNode | None = left
        self.right: CIDRNode | None = right

    def add_data(self, prefix: IPv4Network | IPv6Network, *args):
        """Adds data to node class

        Easy to inherit for things like ROAs
        """

        self.prefix = prefix
