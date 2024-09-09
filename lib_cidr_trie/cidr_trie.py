from abc import ABC, abstractmethod
from ipaddress import IPv4Network, IPv6Network
from typing import Generic, TypeVar

# Assuming CIDRNode is defined elsewhere, and it has a certain interface.
from .cidr_node import CIDRNode

# Define type variables for the prefix and node types
PrefixType = TypeVar("PrefixType", IPv4Network, IPv6Network)

# NOTE: Adding CIDRNode as a generic was causing mypy to flip out
# so I'm removing it


class CIDRTrie(ABC, Generic[PrefixType]):
    """Parent class for trie of CIDRs"""

    def __init__(self, NodeCls: type[CIDRNode] = CIDRNode):
        self.NodeCls: type[CIDRNode] = NodeCls
        self.root: CIDRNode = self.NodeCls()

    def insert(self, prefix: PrefixType, *node_data) -> None:
        """Inserts a prefix into the trie"""
        self._validate_prefix(prefix)
        bits = self._get_binary_str_from_prefix(prefix)
        node = self.root
        for bit in bits[: prefix.prefixlen]:
            if bool(int(bit)):
                if node.right is None:
                    node.right = self.NodeCls()
                node = node.right
            else:
                if node.left is None:
                    node.left = self.NodeCls()
                node = node.left
        node.add_data(prefix, *node_data)

    def __contains__(self, prefix: PrefixType) -> bool:
        """Checks if a prefix is contained within the Trie"""
        return bool(self.get_most_specific_trie_supernet(prefix))

    def get_most_specific_trie_supernet(self, prefix: PrefixType) -> CIDRNode | None:
        """Returns the most specific trie subnet"""
        self._validate_prefix(prefix)
        bits = self._get_binary_str_from_prefix(prefix)
        node = self.root
        most_specific_node = None
        for bit in bits[: prefix.prefixlen]:
            next_node = node.right if bool(int(bit)) else node.left
            if next_node is None:
                return most_specific_node
            elif next_node.prefix is not None:
                most_specific_node = next_node
            node = next_node
        return most_specific_node

    def _validate_prefix(self, prefix: PrefixType) -> None:
        """Checks that prefix is the proper IPV type"""
        if not isinstance(prefix, self.PrefixCls):
            raise TypeError(
                f"Expected prefix type {self.PrefixCls.__name__}, "
                f"got {type(prefix).__name__}"
            )

    def _get_binary_str_from_prefix(self, prefix: PrefixType) -> str:
        """Returns a binary string from a prefix"""

        binary_str = ""
        for _byte in prefix.network_address.packed:
            binary_str += str(bin(_byte))[2:].zfill(8)
        return binary_str

    @property
    @abstractmethod
    def PrefixCls(self) -> type[PrefixType]:
        raise NotImplementedError
