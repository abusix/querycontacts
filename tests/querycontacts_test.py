#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from querycontacts import ContactFinder


class TestQueryContacts(unittest.TestCase):

    def test_simple_lookup(self):
        cfinder = ContactFinder()
        emails = cfinder.find('109.193.88.53')

        self.assertIsNotNone(emails)
        self.assertGreater(len(emails), 0)

        for email in emails:
            self.assertIn('@', email)

    def test_simple_negative(self):
        cfinder = ContactFinder()
        emails = cfinder.find('127.0.0.1')

        self.assertListEqual(emails, ['Abusix ContactDB Test point'])


if __name__ == '__main__':
    unittest.main()
