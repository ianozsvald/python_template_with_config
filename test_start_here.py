#!/usr/bin/env python
"""Tests for start_here"""

import unittest
import start_here
import config

# Run this using:
# $ nosetests
# or
# $ nosetests -s  # show stdout for the print

class Test(unittest.TestCase):
    def setUp(self):
        # we can specify the configuration we need
        self.conf = config.get('dev')

    def test1(self):
        print(self.conf)
        self.assertEqual(start_here.dummy_function(), "Hello")


if __name__ == "__main__":
    unittest.main()
