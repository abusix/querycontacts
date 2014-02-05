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


Examples
--------

    >>> from querycontacts import ContactFinder
    >>> qf = ContactFinder()
    >>> qf.find('1.2.3.4')
    ['abuse@example.com', 'helpdesk@example.com']


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

