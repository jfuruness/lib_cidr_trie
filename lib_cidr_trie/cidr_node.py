from ipaddress import ip_network

class CIDRNode:
    def __init__(self, prefix: ip_network, left: Optional["CIDRNode"] = None, right: Optional["CIDRNode"] = None) -> None:
        """Left is 0. Right is 1. Node in CIDR tree"""

        self.prefix: ip_network = prefix
        self.left: Optional["CIDRNode"] = left
        self.right: Optional["CIDRNode"] = right

    def add_data(self, prefix: ip_network, *args):
        """Adds data to node class

        Easy to inherit for things like ROAs
        """

        self.prefix: ip_network = prefix
