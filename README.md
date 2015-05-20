python_template_with_config
===========================

This is a template for a Python 3.4+ project including:

  * module structure with a `setup.py`, tests/ folder and a utilities/ folder
  * unit test with test environment (via environment variable) allowing configuration via a function call
  * main file with argparse template for command line arguments
  * config module with inherited configurations so you can easily add your own
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

# Overriding the configuration

I've built and used a variety of configuration systems over the years, this is my 'best guess' as to one that works for web microservices (I tend to use Flask), console scripts (e.g. for local usage and Docker) and hacky idea testing.

As it stands if you don't provide any arguments, the Conf will use whatever's coded in its class (see `config.py`):

    $ python start_here.py 
    2015-05-20 16:31:11.625 p16016 {start_here.py:31} INFO - These are our args: Namespace(a_parameter=None, env='dev')
    2015-05-20 16:31:11.625 p16016 {start_here.py:32} INFO - This is our configuration: dev
    2015-05-20 16:31:11.625 p16016 {start_here.py:33} INFO - This is an example log message, logging is configured once config.get() has been called
    2015-05-20 16:31:11.626 p16016 {start_here.py:34} INFO - The value of a_parameter=42

If you pass in an override parameter, that'll be used in preference:

    $ python start_here.py --a_parameter=1
    2015-05-20 16:32:46.517 p16038 {start_here.py:31} INFO - These are our args: Namespace(a_parameter=1, env='dev')
    2015-05-20 16:32:46.517 p16038 {start_here.py:32} INFO - This is our configuration: dev
    2015-05-20 16:32:46.517 p16038 {start_here.py:33} INFO - This is an example log message, logging is configured once config.get() has been called
    2015-05-20 16:32:46.517 p16038 {start_here.py:34} INFO - The value of a_parameter=1

Bare in mind that this assumes that `None` (i.e. not provided) signifies that the parameter isn't being overridden, this might not be the case in your application.

NOTE this override mechanism might be overkill for your needs! Feel free to strip out the `overrides` parameter to simplify everything! Alternatively you might want to pick-up an environment variable for overrides instead of passing them in at the command line.


# Tests

Use `py.test` (or `nosetests` if you're old-skool) to run tests, remember that you can see stdout if you do `py.test -s` which'll include any logging messages.

# Some notes:

  * for unit testing it is useful to add coverage with: https://pypi.python.org/pypi/pytest-cov
  * pip is useful for installing, use `pip freeze > requirements.txt` to free versions of the libraries you're using
  * when logging prefer to use %r or %s in the message rather than more specific types (e.g. %d) as e.g. a %d will raise another exception if None is received but %r can handle the None and a decimal number

# TODO ?

  * in config.py we could auto-discover the available configurations by looking at who inherits from ConfBasic rather than building the list manually
  * it would be nice to check that all configurations have a unique `name` and none are in conflict
