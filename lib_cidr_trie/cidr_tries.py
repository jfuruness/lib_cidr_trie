from ipaddress import IPv4Network, IPv6Network

from .cidr_trie import CIDRTrie


class IPv4CIDRTrie(CIDRTrie[IPv4Network]):
    """Trie of IPv4 CIDRs"""

    PrefixCls = IPv4Network


class IPv6CIDRTrie(CIDRTrie[IPv6Network]):
    """Trie of IPv6 CIDRs"""

    PrefixCls = IPv6Network
