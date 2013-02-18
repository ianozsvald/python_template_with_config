python_template_with_config
===========================

Python coding template including ENV environment variable configuration

WHAT IS THIS PROJECT?

CONSIDER ADDING:
logging - use %r and %s rather than %d, have simple sensible config
    handler = logging.FileHandler('fetch.log')  # use RotatingLogHandler, specify path in config
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
# add email option for errors

suitable subdir structure for setup.py and a setup.py with deployment notes

note that coverage.py is useful 
add empty requirements.txt and note use for pip
http://stackoverflow.com/questions/533048/extend-standard-python-logging-to-include-the-line-number-where-a-log-method-wa/533077#533077  # add log msgs
