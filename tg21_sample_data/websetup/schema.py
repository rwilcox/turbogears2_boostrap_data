# -*- coding: utf-8 -*-
"""Setup the tg21-sample-data application"""

import os
import logging
import transaction
from tg import config

import migrate.versioning.exceptions
import migrate.versioning.api as miapi

from tg21_sample_data import project_root

def setup_schema(command, conf, vars):
    """Place any commands to setup tg21_sample_data here"""
    # Load the models

    # <websetup.websetup.schema.before.model.import>
    from tg21_sample_data import model
    # <websetup.websetup.schema.after.model.import>

    
    # <websetup.websetup.schema.before.metadata.create_all>
    print "Running migrations"
    dburl = config["sqlalchemy.url"]
    repositorypath = os.path.join( project_root(), "model", "migrations" )
    
    try:
        miapi.version_control( dburl, repositorypath )
    except migrate.versioning.exceptions.DatabaseAlreadyControlledError:
        print "database already under version control"
    
    miapi.upgrade(dburl, repositorypath)
