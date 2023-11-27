from ipaddress import IPv4Network, IPv6Network
from typing import Optional


class CIDRNode:
    def __init__(
        self,
        prefix: Optional[IPv4Network | IPv6Network] = None,
        left: Optional["CIDRNode"] = None,
        right: Optional["CIDRNode"] = None,
    ) -> None:
        """Left is 0. Right is 1. Node in CIDR tree"""

        self.prefix: Optional[IPv4Network | IPv6Network] = prefix
        self.left: Optional["CIDRNode"] = left
        self.right: Optional["CIDRNode"] = right

    def add_data(self, prefix: IPv4Network | IPv6Network, *args):
        """Adds data to node class

        Easy to inherit for things like ROAs
        """

        self.prefix = prefix
