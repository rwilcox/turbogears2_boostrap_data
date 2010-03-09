# -*- coding: utf-8 -*-
"""Setup the tg21-sample-data application"""

import logging
from tg import config
from tg21_sample_data import model

import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup tg21_sample_data here"""

    # <websetup.bootstrap.before.auth

    # <websetup.bootstrap.after.auth>
