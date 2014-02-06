.. querycontacts documentation master file, created by
   sphinx-quickstart on Wed Feb  5 12:59:37 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. module:: querycontacts


Usage
-----

::

    usage: querycontacts [-h] [--provider PROVIDER] [--version] ip

    QueryContact - Find the Abuse contact for a IP address

    positional arguments:
    ip                   query network abuse contacts for a given ip address

    optional arguments:
    -h, --help           show this help message and exit
    --provider PROVIDER  change standard network abuse contacts provider.
                        Defaults to abuse-contacts.abusix.org
    --version            show program's version number and exit


Example
-------

::

    >>> from querycontacts import ContactFinder
    >>> qf = ContactFinder()
    >>> qf.find('127.0.0.2')
    ['root@localhost', 'abuse@localhost']

    >>> qf.find('::ffff:7f00:2')
    ['root@localhost']


Installation
------------

::

    pip install querycontacts

API
---


.. autoclass:: ContactFinder
   :members:
   :special-members:



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

