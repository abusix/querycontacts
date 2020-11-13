[![Build Status](https://img.shields.io/github/workflow/status/abusix/querycontacts/test.svg)](https://github.com/abusix/querycontacts/actions/)
[![PyPi Version](https://img.shields.io/pypi/v/querycontacts.svg)](https://pypi.python.org/pypi/querycontacts)
[![PyPi License](https://img.shields.io/pypi/l/querycontacts.svg)](https://pypi.python.org/pypi/querycontacts)
[![PyPi Versions](https://img.shields.io/pypi/pyversions/querycontacts.svg)](https://pypi.python.org/pypi/querycontacts)
[![PyPi Wheel](https://img.shields.io/pypi/wheel/querycontacts.svg)](https://pypi.python.org/pypi/querycontacts)

# querycontacts - Query Abuse Contacts

## Installation

```
pip install querycontacts
```

Starting with version 2.0.0 support for python 2.7 is dropped. This is related to dnspython 2.0.0 also dropping support.

## Command line usage

```
usage: querycontacts [-h] [--provider PROVIDER] [--version] ip

QueryContact - Find the Abuse contact for a IP address

positional arguments:
ip                   query network abuse contacts for a given ip address

optional arguments:
-h, --help           show this help message and exit
--provider PROVIDER  change standard network abuse contacts provider.
                    Defaults to abuse-contacts.abusix.zone
--version            show program's version number and exit
```

### Examples

Show version:

```
$ querycontacts --version
querycontacts 1.1.1
```

Show abuse contact for your IP:

```
$ IP=$(curl ipecho.net/plain)
$ querycontacts $IP
abuse@yourisp.example.com
```

Error when no abuse contact was found:

```
$ querycontacts 127.0.0.1
querycontacts: error: no contacts for 127.0.0.1
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
