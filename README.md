Informational Badges:

[![PyPI version](https://badge.fury.io/py/lib_cidr_trie.svg)](https://badge.fury.io/py/lib_cidr_trie)
![PyPy](https://img.shields.io/badge/PyPy-7.3.17-blue)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lib_cidr_trie)](https://pypi.org/project/lib_cidr_trie/)
![Tests](https://github.com/jfuruness/lib_cidr_trie/actions/workflows/tests.yml/badge.svg)
![Linux](https://img.shields.io/badge/os-Linux-blue.svg)
![macOS Intel](https://img.shields.io/badge/os-macOS_Intel-lightgrey.svg)
![macOS ARM](https://img.shields.io/badge/os-macOS_ARM-lightgrey.svg)

Some Linting Badges (Where I could find them):

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-2A6DBA.svg)](http://mypy-lang.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint/tree/main)
[![try/except style: tryceratops](https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black)](https://github.com/guilatrova/tryceratops)

# If you like this package please leave a github star so I know to continue maintaining it :)

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
cd lib_cidr_trie
pytest lib_cidr_trie
ruff check lib_cidr_trie
ruff format lib_cidr_trie
mypy lib_cidr_trie
```

You can run isolated builds across multiple environments with:

```
cd lib_cidr_trie
tox --skip-missing-interpreters
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

* 1.2.9 Upgrading dependencies and supported Python versions
* 1.2.8 Removed windows classifier from pyproject.toml
* 1.2.7 Updated dependencies and ruff rules
* 1.2.6 Fixed a bug in the pyproject.toml that screwed up non-local installs
* 1.2.5 Updated README
* 1.2.4 Updated docs and test deps
* 1.2.3 Updated package metadata and fixed some formatting for linters
* 1.1.2 Python version updates
* 1.1.1 Dependency updates
* 1.1.0 Removed a few type ignores for mypy, added PrefixType to dunder init
* 1.0.0 Added linters, updated package structure, fixed typing issues
* 0.0.3 Made it easier to subclass CIDRTrie
* 0.0.2 README update
* 0.0.1 First working version

## License
* [lib\_cidr\_trie](#lib_cidr_trie)

BSD License (see license file)
