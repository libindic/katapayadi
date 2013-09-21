#! /usr/bin/python
# -*- coding:utf-8 -*-

import unittest
from katapayadi import getInstance


class TestKatapayadi(unittest.TestCase):

    def setUp(self):
        self.instance = getInstance()

    def test_katapayadi(self):
        self.assertEqual(self.instance.get_number(u"കമല"),351)

    def test_swarasthana(self):
        self.assertEqual(self.instance.get_swarasthanas(1)[2],"Ga1")


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKatapayadi)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
