Usage
=====

    usage: querycontacts [-h] [-z ZONE] [--version] [--provider PROVIDER] [-6] ip

    positional arguments:
      ip                    (query network abuse contacts for given
                            ip address on abuse-contacts.abusix.org)

    optional arguments:
      -h, --help            show this help message and exit
      -z ZONE, --zone ZONE  query only one specific rir zone, supported values:
                            arin, afrinic, lacnic, apnic, ripencc
      --version             show program's version number and exit
      --provider PROVIDER   change standard network abuse contacts provider
      -6                    provided ip address is v6

Examples
--------

    $ querycontacts 2.2.2.8

    $ querycontacts 83.169.16.238

    $ querycontacts -z ripencc 83.169.16.238

    $ querycontacts -6 2001:4800:4860::8844

Installation
------------

    $ pip install querycontacts


