from ipaddress import ip_network

from .cidr_node import CIDRNode


class CIDRTrie:
    """Parent class for trie of CIDRs"""

    node_class = CIDRNode

    def __init__(self):
        # Could be 0.0.0.0/0, for now it's empty
        self.root = CIDRNode()
        assert hasattr(self, "prefix_class"), "No specified IPV"

    def insert(self, prefix, *node_data):
        """Inserts a prefix into the trie"""

        self._validate_prefix(prefix)
        bits = self._get_binary_str_from_prefix(prefix)
        node = self.root
        for bit in bits[:prefix.prefixlen]:
            if bool(int(bit)):
                if node.right is None:
                    node.right = self.node_class()
                node = node.right
            else:
                if node.left is None:
                    node.left = self.node_class()
                node = node.left
        node.add_data(prefix, *node_data)

    def __contains__(self, prefix: ip_network):
        """Checks if a prefix is contained within the Trie"""

        return bool(self.get_most_specific_trie_supernet(prefix))

    def get_most_specific_trie_supernet(self, prefix: ip_network):
        """Returns the most specific trie subnet"""

        self._validate_prefix(prefix)
        bits = self._get_binary_str_from_prefix(prefix)
        node = self.root
        # Default to None
        most_specific_node = self.root.prefix
        for bit in bits[:prefix.prefixlen]:
            # Get the next node in the sequence
            next_node = node.right if bool(int(bit)) else node.left
            # Reached edge of tree
            if next_node is None:
                return most_specific_node
            # New most specific node
            elif next_node.prefix is not None:
                most_specific_node = next_node
            node = next_node

        return most_specific_node

    def _validate_prefix(self, prefix: ip_network):
        """Checks that prefix is the proper IPV type"""

        if not isinstance(prefix, self.prefix_class):
            raise Exception("Must be an {self.prefix_class.__name__}")

    def _get_binary_str_from_prefix(self, prefix: ip_network):
        """Returns a binary string from a prefix"""

        binary_str = ""
        for _byte in prefix.network_address.packed:
            # https://stackoverflow.com/a/339013/8903959
            # Convert to binary, then remove the 0b, then fill w/zeroes
            binary_str += str(bin(_byte))[2:].zfill(8)
        return binary_str
