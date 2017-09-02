#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Katapayadi


class KatapayadiTest(TestCase):

    def setUp(self):
        super(KatapayadiTest, self).setUp()
        self.katapayadi = Katapayadi()

    def test_katapayadi(self):
        self.assertEqual(self.katapayadi.get_number(u"കമല"),351)

    def test_swarasthana(self):
        self.assertEqual(self.katapayadi.get_swarasthanas(1)[2],"Ga1")
