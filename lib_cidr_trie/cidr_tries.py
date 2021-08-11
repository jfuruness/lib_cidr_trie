from ipaddress import IPv4Network, IPv6Network

from .cidr_trie import CIDRTrie


class IPv4CIDRTrie(CIDRTrie):
    """Trie of IPv4 CIDRs"""

    prefix_class = IPv4Network


class IPv6CIDRTrie(CIDRTrie):
    """Trie of IPv6 CIDRs"""

    prefix_class = IPv6Network
