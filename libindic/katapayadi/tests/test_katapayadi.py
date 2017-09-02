#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Katapayadi


class KatapayadiTest(TestCase):

    def setUp(self):
        super(KatapayadiTest, self).setUp()
        self.katapayadi = Katapayadi()

    def test_katapayadi(self):
        self.assertEqual(self.katapayadi.get_number(u"കമല"), 351)
        self.assertEqual(self.katapayadi.get_number(u"വ്യാജം"), 81)
        self.assertEqual(self.katapayadi.get_number(u"സത്യം"), 17)
        self.assertEqual(self.katapayadi.get_number(u"കൃഷ്ണ"), 51)
        self.assertEqual(self.katapayadi.get_number(u"ലീല"), 33)
        self.assertEqual(self.katapayadi.get_number(u"മനസ്സു്"), 705)
        self.assertEqual(self.katapayadi.get_number(u"കാമം"), 51)
        self.assertEqual(self.katapayadi.get_number(u"മോക്ഷം"), 65)

    def test_swarasthana(self):
        self.assertEqual(self.katapayadi.get_swarasthanas(1)[2], "Ga1")
