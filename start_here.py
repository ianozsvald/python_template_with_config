"""1 liner to explain this project"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.python.org/dev/peps/pep-0263/
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
    print "These are our args:"
    print args
    print "{} {}".format(args.positional_arg, args.optional_arg)
