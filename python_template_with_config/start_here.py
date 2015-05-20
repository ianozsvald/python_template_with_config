#!/usr/bin/env python
"""1 liner to explain this project"""
import argparse
import logging
from python_template_with_config import config
from python_template_with_config import another_module  # just to show how to import another module in this package


# See the README for notes on running this using either:
# arguments via __main__
# a configuration environment variable


def dummy_function():
    """Delete this dummy function, it is here for the unittests"""
    return "Hello"


if __name__ == "__main__":
    # Create an argument parser which also shows the defaults when --help is
    # called
    parser = argparse.ArgumentParser(description='Project description for this prototype...',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # These two lines show a positional (mandatory) argument and an optional argument
    # parser.add_argument('positional_arg', type=str, help='required positional argument')
    parser.add_argument('--env', default="dev", help='optional configuration argument')
    parser.add_argument('--a_parameter', type=int, default=None, help='some other parameter that is already in the Conf')
    args = parser.parse_args()

    conf = config.get(args.env, overrides=vars(args))  # Note that the environment is optional (it can use a config environment instead)
    logging.info("These are our args: {}".format(args))
    logging.info("This is our configuration: {}".format(conf))
    logging.info("This is an example log message, logging is configured once config.get() has been called")
    logging.info("The value of a_parameter={}".format(conf.a_parameter))
