from ipaddress import IPv4Network, ip_network

from lib_cidr_trie import IPv4CIDRTrie


def test_tree():
    trie = IPv4CIDRTrie()
    cidrs = [ip_network(x) for x in ["1.2.0.0/16", "1.2.3.0/24", "1.2.3.4"]]
    for cidr in cidrs:
        # for mypy
        assert isinstance(cidr, IPv4Network)
        trie.insert(cidr)
    for cidr in cidrs:
        assert isinstance(cidr, IPv4Network)
        assert cidr in trie
        node = trie.get_most_specific_trie_supernet(cidr)
        assert node is not None
        assert node.prefix == cidr

    invalid_cidrs = [ip_network(x) for x in ["1.0.0.0/8", "255.255.255.255"]]
    for invalid_cidr in invalid_cidrs:
        # for mypy
        assert isinstance(invalid_cidr, IPv4Network)
        assert invalid_cidr not in trie
        assert trie.get_most_specific_trie_supernet(invalid_cidr) is None

    assert IPv4Network("1.2.4.0/24") in trie
    assert IPv4Network("1.2.0.255") in trie
    assert IPv4Network("1.3.0.0/16") not in trie
