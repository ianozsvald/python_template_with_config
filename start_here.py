#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""1 liner to explain this project"""
import argparse
import config

# Configuration options, we can pass an arg or an environment variable
# $ python start_here.py hello --configuration=dev_windows
# $ CONFIG=windows_dev python start_here.py hello
# or in the code we call config.get(<myconfiguration>)

def dummy_function():
    """Delete this dummy function, it is here for the test_start_here's unittests"""
    return "Hello"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Project description')
    parser.add_argument('positional_arg', type=str, help='required positional argument')
    parser.add_argument('--configuration', '-c', default="dev", help='optional configuration argument')
    args = parser.parse_args()
    print("These are our args:", args)
    conf = config.get(args.configuration)
    print("Using this configuration:", conf)

    config.logging.info("This is an example log message")
