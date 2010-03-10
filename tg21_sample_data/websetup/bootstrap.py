# -*- coding: utf-8 -*-
"""Setup the tg21-sample-data application"""

import sys
import logging
from tg import config
from tg21_sample_data.model import *
import transaction
import bootstrap_data

def bootstrap(command, conf, vars):
    """Place any commands to setup tg21_sample_data here"""

    # <websetup.bootstrap.before.auth

    # <websetup.bootstrap.after.auth>
        
    # States!
    # This is the normal way to do bootstrap data in a TG2.1 app, and it's OK
    # it does, however, have the following limitations:
    #
    # 1) If you run `paster setup-app` twice you'll get 51 * 2 = 102 records (for our example of having bootstrap data of the US states)
    # 2) If you have new sample data to add to this file (say a list of timezones)
    #     you have to rerun `paster setup-app` to get the new bootstrap data...
    #     and you'll get duplicate data
    # 3) if you had any UNIQUE database requirements, these barf when you try to
    #     feed them those duplicate records
    #
    # 4) Tansgental to all this, an application might have a requirement for sample data:
    #    data that is used in development, and early alpha testing, to set up the system.
    #    Things that are normally added to this file when you enable the auth framework,
    #    for example. Or data from user stories and personas, if your customers write acceptance tests
    #    and want to entities from these stories already created.
    #
    # One way to avoid items 1-3 is to check to see if you have a set of data before adding it
    # to the session. You could use the following pattern:
    #
    # if len( DBsession.query(State).filter_by(postal_code = "AK") ) == 0:
    #   DBSession.add( State("Alaska", "AK") )
    #
    # but this smells. So we need something better
    #
    # We could take a page from SQLAlchemy-migrate's book here: files
    # with bootstrap data that are loaded incrementally.
    #
    # (We actually deviate a bit from SQLAlchemy-migrate a bit here: we create one record for every
    # data migration, instead of just counting the migration number. Experiances in Rails tell me to avoid
    # the former, and prefer the latter: WD-rpw 03-09-2010)
    #
    # I think the same "data migration" files can be used for cases 1-3 above, in addtion to case 4,
    # as long as the data migration files are passed the current config (where the programmer can check
    # a setting and maybe do nothing if it's set a certain way)
    
    # So, we load the data migrations from websetup/bootstrap_data/bootstrap_*.py
    # and execute each module's upgrade() or downgrade function as required
    DataMigration.run_all(conf)
