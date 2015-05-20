python_template_with_config
===========================

This is a template for a simple Python 3.4+ project including:

  * unit test with test environment (via environment variable) or configure via a function call
  * main file with argparse template for command line arguments
  * config folder with simple structure for testing and production environments
  * logging configured with ISO-8601 date (parseable by dateutil.parser), process number, file and line number

# Installation

    $ python setup.py develop  # install locally, it symlinks back to this folder
    $ (python setup.py install)  # probably you *don't want to do this* as this project is useless by itself (once you've customised it, maybe this is what you want to do...)

# Usage

Python coding template including ENV environment variable configuration::

    $ python start_here.py --env=dev
    $ CONFIG=dev python start_here.py 

Using `--help` will show the default arguments and all your options:

    $ python start_here.py --help
    usage: start_here.py [-h] [--env ENV]

    Project description for this prototype...

    optional arguments:
    -h, --help  show this help message and exit
    --env ENV   optional configuration argument (default: dev)


# Tests

Use `py.test` (or `nosetests` if you're old-skool) to run tests, remember that you can see stdout if you do `py.test -s` which'll include any logging messages.

Some notes:

  * for unit testing it is useful to add Ned Batchelder's coverage
  * pip is useful for installing, use `pip freeze > requirements.txt` to free versions of the libraries you're using
  * when logging prefer to use %r or %s in the message rather than more specific types (e.g. %d) as e.g. a %d will raise another exception if None is received but %r can handle the None and a decimal number
