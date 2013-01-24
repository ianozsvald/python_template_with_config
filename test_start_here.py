"""Tests for start_here"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://www.python.org/dev/peps/pep-0263/
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
