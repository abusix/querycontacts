'''
querycontacts: query network abuse contacts for a given ip address on
abuse-contacts.abusix.zone

Copyright 2013 by abusix GmbH
Author: abusix GmbH
License: GPLv3

'''

from dns import resolver
from dns.reversename import from_address as reversename
from dns.name import from_text as dnsname

import ipaddress

from ._version import __version__


class ContactFinder(object):

    '''
    Contact Finder
    '''

    def __init__(self, provider='abuse-contacts.abusix.zone'):
        '''
        Init

        :param provider: Abuse contact lookup provider
        :type provider: string
        '''
        self.set_provider(provider)
        self.resolver = resolver.get_default_resolver()

    def set_provider(self, provider):
        '''
        set the provider for a specific path

        :param provider: Abuse contact lookup provider
        :type provider: string
        '''
        self.provider = dnsname(provider)

    def find(self, ip):
        '''
        Find the abuse contact for a IP address

        :param ip: IPv4 or IPv6 address to check
        :type ip: string

        :returns: emails associated with IP
        :rtype: list
        :returns: none if no contact could be found
        :rtype: None

        :raises: :py:class:`ValueError`: if ip is not properly formatted
        '''
        ip = ipaddress.ip_address(ip)
        rev = reversename(ip.exploded)
        revip, _ = rev.split(3)
        lookup = revip.concatenate(self.provider).to_text()

        contacts = self._get_txt_record(lookup)
        if contacts:
            return contacts.split(',')

    def _get_txt_record(self, name):
        try:
            answers = self.resolver.resolve(name, 'TXT')
        except (resolver.NXDOMAIN, resolver.NoAnswer):
            return

        for answer in answers:
            return ''.join([answer_string.decode('utf-8')
                            for answer_string in answer.strings])
