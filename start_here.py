#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""1 liner to explain this project"""
from __future__ import division  # 1/2 == 0.5, as in Py3
from __future__ import absolute_import  # avoid hiding global modules with locals
from __future__ import print_function  # force use of print("hello")
from __future__ import unicode_literals  # force unadorned strings "" to be unicode without prepending u""
import argparse
import config  # assumes env var PYTHON_TEMPLATE_CONFIG is configured

# Usage:
# $ PYTHON_TEMPLATE_CONFIG=production python start_here.py --help
# $ PYTHON_TEMPLATE_CONFIG=production python start_here.py hello -o bob

def dummy_function():
    """Delete this dummy function"""
    return "Hello"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Project description')
    parser.add_argument('positional_arg', help='required positional argument')
    parser.add_argument('--optional_arg', '-o', help='optional argument', default="Ian")

    args = parser.parse_args()
    print("These are our args:")
    print(args)
    print("{} {}".format(args.positional_arg, args.optional_arg))

    config.logging.info("This is an example log message")
