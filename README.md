python_template_with_config
===========================

This is a template for a simple Python project including:

  * unit test with test environment (via environment variable)
  * main file with argparse template for command line arguments
  * config folder with simple structure for testing and production environments
  * __future__ imports to make Python 3 porting easier
  * logging configured with ISO-8601 date (parseable by dateutil.parser), process number, file and line number

Python coding template including ENV environment variable configuration::

    $ PYTHON_TEMPLATE_CONFIG=testing python test_start_here.py  # run unit tests

To run the main code use::

    $ PYTHON_TEMPLATE_CONFIG=production python start_here.py --help

Note that 'testing' will be assumed in config/__init__.py if PYTHON_TEMPLATE_CONFIG is not available as an environment variable.

Some notes:

  * for unit testing it is useful to add nosetests (`pip install nose`) and Ned Batchelder's `coverage.py`.
  * pip is useful for installing, use `pip freeze > requirements.txt` to free versions of the libraries you're using
  * when logging prefer to use %r or %s in the message rather than more specific types (e.g. %d) as e.g. a %d will raise another exception if None is received but %r can handle the None and a decimal number

CONSIDER ADDING:

  * suitable subdir structure for setup.py and a setup.py with deployment notes
