from setuptools import setup, find_packages
import sys

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# https://stackoverflow.com/a/58534041/8903959
setup(
    name='lib_cidr_trie',
    author="Justin Furuness",
    author_email="jfuruness@gmail.com",
    version="0.0.3",
    url='https://github.com/jfuruness/lib_cidr_trie.git',
    license="BSD",
    description="Creates a CIDR trie",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["Furuness", "prefix", "cidr", "inet", "trie", "cidr-trie",
              "roas", "roas-trie", "ROA", "ROAs", "ROAs-trie"],
    include_package_data=True,
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        "ip_address",
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'],
    entry_points={},
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
