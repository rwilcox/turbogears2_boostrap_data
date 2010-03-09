# -*- coding: utf-8 -*-
"""WSGI environment setup for tg21-sample-data."""

from tg21_sample_data.config.app_cfg import base_config

__all__ = ['load_environment']

#Use base_config to setup the environment loader function
load_environment = base_config.make_load_environment()
