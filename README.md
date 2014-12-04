python_template_with_config
===========================

This is a template for a simple Python 3.4+ project including:

  * unit test with test environment (via environment variable) or configure via a function call
  * main file with argparse template for command line arguments
  * config folder with simple structure for testing and production environments
  * logging configured with ISO-8601 date (parseable by dateutil.parser), process number, file and line number

Python coding template including ENV environment variable configuration::

    $ python start_here.py hello --configuration=dev_windows
    $ CONFIG=windows_dev python start_here.py hello
    # or requests config.get(<myconf>) in your code, see start_here.__main__

Tests (e.g. `test_start_here.py`) can ask for a testing configuration in `setUp`, allowing per-test configurations.

Some notes:

  * for unit testing it is useful to add nosetests (`pip install nose`) and Ned Batchelder's `coverage.py`.
  * pip is useful for installing, use `pip freeze > requirements.txt` to free versions of the libraries you're using
  * when logging prefer to use %r or %s in the message rather than more specific types (e.g. %d) as e.g. a %d will raise another exception if None is received but %r can handle the None and a decimal number
