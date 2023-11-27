# lib\_cidr\_trie
This package contains a trie of prefixes for fast lookups

* [Usage](#usage)
* [Installation](#installation)
* [Testing](#testing)
* [Development/Contributing](#developmentcontributing)
* [History](#history)
* [Licence](#license)

## Usage
* [lib\_cidr\_trie](#lib_cidr_trie)

```python
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
    assert node is not None and node.prefix == cidr

invalid_cidrs = [ip_network(x) for x in ["1.0.0.0/8", "255.255.255.255"]]
for invalid_cidr in invalid_cidrs:
    # for mypy
    assert isinstance(invalid_cidr, IPv4Network)
    assert invalid_cidr not in trie
    assert trie.get_most_specific_trie_supernet(invalid_cidr) is None

assert IPv4Network("1.2.4.0/24") in trie
assert IPv4Network("1.2.0.255") in trie
assert IPv4Network("1.3.0.0/16") not in trie
```

## Installation
* [lib\_cidr\_trie](#lib_cidr_trie)

Install python and pip if you have not already. Then run:

```bash
pip3 install lib_cidr_trie
```

This will install the package and all of it's python dependencies.

If you want to install the project for development:
```bash
git clone https://github.com/jfuruness/lib_cidr_trie.git
cd lib_cidr_trie
pip3 install -e .[test]
pre-commit install
```

To test the development package: [Testing](#testing)


## Testing
* [lib\_cidr_trie](#lib_cidr_trie)

To test the package after installation:

```
cd roa_collector
pytest roa_collector
ruff roa_collector
black roa_collector
mypy roa_collector
```

If you want to run it across multiple environments, and have python 3.10 and 3.11 installed:

```
cd roa_collector
tox
```

## Development/Contributing
* [lib\_cidr\_trie](#lib_cidr_trie)

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request
6. Email me at jfuruness@gmail.com because I don't check github messages

## History
* [lib\_cidr\_trie](#lib_cidr_trie)
* 1.1.0 Removed a few type ignores for mypy, added PrefixType to dunder init
* 1.0.0 Added linters, updated package structure, fixed typing issues
* 0.0.3 Made it easier to subclass CIDRTrie
* 0.0.2 README update
* 0.0.1 First working version

## License
* [lib\_cidr\_trie](#lib_cidr_trie)

BSD License (see license file)
