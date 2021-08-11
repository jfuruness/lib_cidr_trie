# lib\_cidr\_trie
This package contains a trie of prefixes for fast lookups

* [Description](#package-description)
* [Usage](#usage)
* [Installation](#installation)
* [Testing](#testing)
* [Development/Contributing](#developmentcontributing)
* [History](#history)
* [Credits](#credits)
* [Licence](#license)
* [TODO](#todo)

## Package Description
* [lib\_cidr\_trie](#lib_cidr_trie)

This package contains a trie of prefixes for fast lookups

## Usage
* [lib\_cidr\_trie](#lib_cidr_trie)

```python
from ipaddress import ip_network

from lib_cidr_trie import IPv4CIDRTrie, IPv6CIDRTrie


trie = IPv4CIDRTrie()
cidrs = [ip_network(x) for x in ["1.2.0.0/16", "1.2.3.0/24", "1.2.3.4"]]
for cidr in cidrs:
	trie.insert(cidr)
for cidr in cidrs:
	assert cidr in trie
	assert trie.get_most_specific_trie_supernet(cidr).prefix == cidr

invalid_cidrs = [ip_network(x) for x in ["1.0.0.0/8", "255.255.255.255"]]
for invalid_cidr in invalid_cidrs:
	assert invalid_cidr not in trie
	assert trie.get_most_specific_trie_supernet(invalid_cidr) is None

assert ip_network("1.2.4.0/24") in trie
assert ip_network("1.2.0.255") in trie
assert ip_network("1.3.0.0/16") not in trie
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
python3 setup.py develop
```

To test the development package: [Testing](#testing)


## Testing
* [lib\_cidr_trie](#lib_cidr_trie)

You can test the package if in development by moving/cd into the directory where setup.py is located and running:
(Note that you must have all dependencies installed first)
```python3 setup.py test```


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
* 0.0.1 First working version

## Credits
* [lib\_cidr\_trie](#lib_cidr_trie)


## License
* [lib\_cidr\_trie](#lib_cidr_trie)

BSD License (see license file)

## TODO
* [lib\_cidr\_trie](#lib_cidr_trie)
* Needs better testing
* Would be nice to have some traversal funcs
