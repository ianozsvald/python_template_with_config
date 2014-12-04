""""""
import os
import logging

# environment variable for configuration
CONFIG_ENV_VAR = "CONFIG"

# Simple logging configuration, an example output might be:
# 2013-06-03 15:07:55.740 p7470 {start_here.py:31} INFO - This is an example log message
LOG_FILE_NAME = "log.log"
# The date format is ISO 8601, format includes a decimal separator for
# milliseconds (not the default comma) as dateutil.parser cannot read the
# command but it can read the decimal separator (both are allowed in ISO 8601)
logging.basicConfig(filename=LOG_FILE_NAME, level=logging.DEBUG, format='%(asctime)s.%(msecs)d p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# note that it might be useful to use the ConcurrentLogHandler or
# RotatingLogHandler here (either require some more setup)

# names of configurations (both passed as 'configuration' or via environment
# variable)
CONFIG_DEV = "dev"
CONFIG_DEV_WINDOWS = "dev_windows"


def get(configuration=None):
    """Return a configuration based on name or environment variable"""
    if configuration is None:
        configuration = os.getenv(CONFIG_ENV_VAR)

    if configuration == CONFIG_DEV:
        conf = {"name": CONFIG_DEV}
        return conf

    if configuration == CONFIG_DEV_WINDOWS:
        conf = {"name": CONFIG_DEV_WINDOWS}
        return conf

    assert False, "You must choose a configuration"
