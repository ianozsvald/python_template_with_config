#!/usr/bin/env python
"""Tests for start_here"""

import unittest
import logging
from python_template_with_config import start_here
from python_template_with_config import config

# Run this using:
# $ nosetests
# or
# $ nosetests -s  # show stdout for the print

A_PARAMETER = 99


class Test(unittest.TestCase):
    def setUp(self):
        # get a config object (this is optional, remove if you don't need it)
        self.conf = config.get('test')

    def test1(self):
        print(self.conf)
        logging.info("Testing some very basic things")
        self.assertEqual(start_here.dummy_function(), "Hello")
        self.assertEqual(self.conf.name, "test")
        self.assertEqual(self.conf.a_parameter, A_PARAMETER)


if __name__ == "__main__":
    unittest.main()
