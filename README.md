python_template_with_config
===========================

Python coding template including ENV environment variable configuration

PYTHON_TEMPLATE_CONFIG=production python test_start_here.py

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


consider use of:
```
from __future__ import division  # 1/2 == 0.5, as in Py3
from __future__ import absolute_import  # avoid hiding global modules with locals
from __future__ import print_function  # force use of print("hello") 
from __future__ import unicode_literals  # force unadorned strings "" to be unicode without prepending u""
```
