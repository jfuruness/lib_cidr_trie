from abc import ABC, abstractmethod
from ipaddress import ip_network
from typing import Optional

from .cidr_node import CIDRNode


class CIDRTrie(ABC):
    """Parent class for trie of CIDRs"""

    def __init__(self, NodeCls: type[CIDRNode] = CIDRNode):
        self.NodeCls: type[CIDRNode] = CIDRNode
        # Could be 0.0.0.0/0, for now it's empty
        self.root: CIDRNode = self.NodeCls

    def insert(self, prefix: ip_network, *node_data) -> None:
        """Inserts a prefix into the trie"""

        # Make sure prefix is IPV4 if it's an IPV4 tree or IPV6
        self._validate_prefix(prefix)
        # Turn the prefix into bits
        bits = self._get_binary_str_from_prefix(prefix)
        node = self.root
        # Only go to the bits up to the prefix length
        # after which the bits are meaningless
        for bit in bits[:prefix.prefixlen]:
            # If it's a 1, go to the right
            if bool(int(bit)):
                if node.right is None:
                    node.right = self.NodeCls()
                node = node.right
            # If bit is a zero, go to the left
            else:
                if node.left is None:
                    node.left = self.NodeCls()
                node = node.left
        # Add the data to the very last node
        node.add_data(prefix, *node_data)

    def __contains__(self, prefix: ip_network) -> bool:
        """Checks if a prefix is contained within the Trie"""

        return bool(self.get_most_specific_trie_supernet(prefix))

    def get_most_specific_trie_supernet(self, prefix: ip_network) -> Optional[CIDRNode]:
        """Returns the most specific trie subnet"""

        self._validate_prefix(prefix)
        bits = self._get_binary_str_from_prefix(prefix)
        node = self.root
        # Default to None
        most_specific_node = None
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

    def _validate_prefix(self, prefix: ip_network) -> None:
        """Checks that prefix is the proper IPV type"""

        if not isinstance(prefix, self.PrefixCls):
            raise TypeError("Must be an {self.PrefixCls.__name__}")

    def _get_binary_str_from_prefix(self, prefix: ip_network) -> str:
        """Returns a binary string from a prefix"""

        binary_str = ""
        for _byte in prefix.network_address.packed:
            # https://stackoverflow.com/a/339013/8903959
            # Convert to binary, then remove the 0b, then fill w/zeroes
            binary_str += str(bin(_byte))[2:].zfill(8)
        return binary_str

    @property
    @abstractmethod
    def PrefixCls(self) -> type[ip_network]:
        raise NotImplementedError
