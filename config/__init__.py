"""Configuration provided by 'import config' and PYTHON_TEMPLATE_CONFIG env var"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

# Read PYTHON_TEMPLATE_CONFIG environment variable (raise error if missing or badly
# configured), use this to decide on our config and import the relevant python
# file

# This assumes that locally we have suitable python files e.g. production.py,
# testing.py
CONFIG_ENV_VAR = "PYTHON_TEMPLATE_CONFIG"
CONFIG_ENV_VAR_PRODUCTION = "production"
CONFIG_ENV_VAR_TESTING = "testing"
config_set = False  # only set to True if we have find a valid ENV VAR
config_choice = os.getenv(CONFIG_ENV_VAR)
if config_choice == CONFIG_ENV_VAR_PRODUCTION:
    from production import *
    config_set = True
if config_choice == CONFIG_ENV_VAR_TESTING:
    from testing import *
    config_set = True
if not config_set:
    raise ValueError("ALERT! ENV VAR \"{}\" must be set e.g. \"export {}={}\"".format(CONFIG_ENV_VAR, CONFIG_ENV_VAR, CONFIG_ENV_VAR_TESTING))
