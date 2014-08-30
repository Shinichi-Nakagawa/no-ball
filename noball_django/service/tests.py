#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


import unittest
from service.stats import Stats


class TestStats(unittest.TestCase):
    """
    Stats Class Tests
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_single(self):
        """
        single test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        self.assertEqual(single, 225)

    def test_tb(self):
        """
        Total bases test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        tb = Stats.tb(single, 8, 24, 5)
        self.assertEqual(tb, 320)

    def test_rc(self):
        """
        Run created test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        rc = Stats.rc(262, 49, 4, 11, 6, 3, 2, 36, 63, 704, 19, single, 24, 5, 8)
        self.assertEqual(rc, 137)

    def test_rc27(self):
        """
        Run created 27 test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        rc = Stats.rc(262, 49, 4, 11, 6, 3, 2, 36, 63, 704, 19, single, 24, 5, 8)
        rc27 = Stats.rc27(rc, 704, 262, 2, 3, 11, 6)
        self.assertEqual(rc27, 8)


if __name__ == '__main__':
    unittest.main()

