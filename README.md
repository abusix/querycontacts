[![Build Status](https://img.shields.io/travis/abusix/querycontacts/master.svg)](https://travis-ci.org/abusix/querycontacts)
[![Test Coverage](https://img.shields.io/coveralls/github/abusix/querycontacts/master.svg)](https://coveralls.io/github/abusix/querycontacts)
[![PyPi Version](https://img.shields.io/pypi/v/querycontacts.svg)](https://pypi.python.org/pypi/querycontacts)
[![PyPi License](https://img.shields.io/pypi/l/querycontacts.svg)](https://pypi.python.org/pypi/querycontacts)
[![PyPi Versions](https://img.shields.io/pypi/pyversions/querycontacts.svg)](https://pypi.python.org/pypi/querycontacts)
[![PyPi Wheel](https://img.shields.io/pypi/wheel/querycontacts.svg)](https://pypi.python.org/pypi/querycontacts)

# querycontacts - Query Abuse Contacts

ahocorapy is a pure python implementation of the Aho-Corasick Algorithm.
Given a list of keywords one can check if at least one of the keywords exist in a given text in linear time.

## Installation

```
pip install querycontacts
```

## Command line usage

```
usage: querycontacts [-h] [--provider PROVIDER] [--version] ip

QueryContact - Find the Abuse contact for a IP address

positional arguments:
ip                   query network abuse contacts for a given ip address

optional arguments:
-h, --help           show this help message and exit
--provider PROVIDER  change standard network abuse contacts provider.
                    Defaults to abuse-contacts.abusix.org
--version            show program's version number and exit
```

### Example

```
querycontacts 127.0.0.1
```

## Library usage
```
>>> from querycontacts import ContactFinder
>>> qf = ContactFinder()
>>> qf.find('127.0.0.2')
['root@localhost', 'abuse@localhost']

>>> qf.find('::ffff:7f00:2')
['root@localhost']
```