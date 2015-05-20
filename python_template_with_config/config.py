""""""
import os
import abc
import sys
import logging


# environment variable for configuration
CONFIG_ENV_VAR = "CONFIG"


def configure_logging(log_level):
    # configure logging to stdout
    root = logging.getLogger()
    root.setLevel(log_level)

    # only add a new handler if we've not set one yet
    if len(root.handlers) == 0:
        fmt = '%(asctime)s.%(msecs)d p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
        datefmt = '%Y-%m-%d %H:%M:%S'

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(log_level)

        formatter = logging.Formatter(fmt, datefmt=datefmt)
        ch.setFormatter(formatter)
        root.addHandler(ch)


class ConfBasic(abc.ABC):
    """Abstract Base Class that defines some of the basics for our configuration"""
    name = "conf_basic_ABC"

    def __init__(self):
        configure_logging(logging.DEBUG)

    def __repr__(self):
        """Simplest representation of what a configuration looks like"""
        return self.name


class ConfDev(ConfBasic):
    """Configuration for development scenario"""
    name = "dev"

    def __init__(self):
        super().__init__()
        self.a_parameter = 42


class ConfTest(ConfBasic):
    """Example 2nd configuration, a test scenario"""
    name = "test"

    def __init__(self):
        super().__init__()
        self.a_parameter = 99

available_configurations = [ConfDev, ConfTest]


def get(configuration=None):
    """Return a configuration based on name or environment variable"""
    if configuration is None:
        configuration = os.getenv(CONFIG_ENV_VAR)

    # look through the available configurations, find the
    # match and instantiate it
    for c in available_configurations:
        if c.name == configuration:
            conf = c()
            return conf

    configuration_names = [c.name for c in available_configurations]
    print("No configuration matches to '{}', you must pass in a configuration from {}".format(configuration, configuration_names))
    raise ValueError("No matching configuration")
