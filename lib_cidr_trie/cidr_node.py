from ipaddress import IPv4Network, IPv6Network

class CIDRNode:
    def __init__(self, prefix=None, left=None, right=None):
        """Left is 0. Right is 1."""

        self.prefix = prefix
        self.left = left
        self.right = right


class CIDRTrie:
    """Parent class for trie of CIDRs"""

    node_class = CIDRNode

    def __init__(self):
        self.root = CIDRNode()
        assert hasattr(self, "ipv_class"), "No specified IPV"

    def insert(self, prefix: ip_network, val=None):
        """Inserts a prefix into the trie"""

        self._validate_prefix(prefix)
        bits = self._get_binary_str_from_prefix(prefix)
        node = self.root
        for bit in bits[:prefix.prefixlen]:
            if bool(int(bit)):
                if node.right is None:
                    node.right = CIDRTrie.node_class()
                node = node.right
            else:
                if node.left is None:
                    node.left = CIDRTrie.node_class()
                node = node.left
        node.prefix = prefix

    def __contains__(self, prefix: ip_network):
        """Checks if a prefix is contained within the Trie"""

        if self.get_most_specific_contained_or_equal(prefix) is None:
            return True
        else:
            return False

    def get_most_specific_contained_or_equal(self, prefix: ip_network):
        """Returns the most specific superprefix"""

        self._validate_prefix(prefix)
        bits = self._get_binary_str_from_prefix(prefix)
        node = self.root
        for bit in bits[:prefix.prefixlen]:
            # Get the next node in the sequence
            next_node = node.right if bool(int(bit)) else node.left
            # Prefix is more specific than anything in trie
            if next_node is None:
                return node
            node = next_node
        # Prefix is exactly the same as what exists in trie
        if node.prefix is not None:
            return node
        # This prefix is a superprefix
        else:
            return None

    def _validate_prefix(self, prefix: ip_network):
        """Checks that prefix is the proper IPV type"""

        if not isinstance(prefix, self.prefix_cls):
            raise Exception("Must be an {self.prefix_cls.__name__}")

    def _get_binary_str_from_prefix(self, prefix: ip_network):
        """Returns a binary string from a prefix"""

        binary_str = ""
        for _byte in prefix.network_address.packed:
            # https://stackoverflow.com/a/339013/8903959
            # Convert to binary, then remove the 0b, then fill w/zeroes
            binary_str += str(bin(_byte))[2:].zfill(4)
        return binary_str

class IPv4CIDRTrie(CIDRTrie):
    """Trie of IPv4 CIDRs"""

    prefix_cls = IPv4Address

class IPv6CIDRTrie(CIDRTrie):
    """Trie of IPv6 CIDRs"""

    prefix_cls = IPv6Address
