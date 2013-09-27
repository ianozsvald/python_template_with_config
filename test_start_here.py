#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for start_here"""

import unittest
import start_here

# Usage:
# $ PYTHON_TEMPLATE_CONFIG=testing python test_start_here.py
# $ PYTHON_TEMPLATE_CONFIG=testing python -m unittest discover


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(start_here.dummy_function(), "Hello")


if __name__ == "__main__":
    unittest.main()
