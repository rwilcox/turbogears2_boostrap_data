# -*- coding: utf-8 -*-
"""Setup the tg21-sample-data application"""

import logging
from tg import config
from tg21_sample_data.model import *
import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup tg21_sample_data here"""

    # <websetup.bootstrap.before.auth

    # <websetup.bootstrap.after.auth>
        
    # States!
    # This is the normal way to do bootstrap data in a TG2.1 app, and it's OK
    # it does, however, have the following limitations:
    #
    # 1) If you run `paster setup-app` twice you'll get 52 * 2 = 104 records
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
    
    DBSession.add( State("Alaska", "AK") )
    DBSession.add( State("Alabama" , "AL") )
    DBSession.add( State("Arkansas" , "AR") )
    DBSession.add( State("Arizona" , "AZ") )
    DBSession.add( State("California" , "CA") )
    DBSession.add( State("Colorado" , "CO") )
    DBSession.add( State("Connecticut" , "CT") )
    DBSession.add( State("Delaware" , "DE") )
    DBSession.add( State("District of Columbia" , "DC") )
    DBSession.add( State("Florida" , "FL") )
    DBSession.add( State("Georgia" , "GA") )
    DBSession.add( State("Hawaii" , "HI") )
    DBSession.add( State("Iowa" , "IA") )
    DBSession.add( State("Idaho" , "ID") )
    DBSession.add( State("Illinois" , "IL") )
    DBSession.add( State("Indiana" , "IN") )
    DBSession.add( State("Kansas" , "KS") )
    DBSession.add( State("Kentucky" , "KY") )
    DBSession.add( State("Louisiana" , "LA") )
    DBSession.add( State("Massachusetts" , "MA") )
    DBSession.add( State("Maryland" , "MD") )
    DBSession.add( State("Maine" , "ME") )
    DBSession.add( State("Michigan" , "MI") )
    DBSession.add( State("Minnesota" , "MN") )
    DBSession.add( State("Mississippi" , "MS") )
    DBSession.add( State("Missouri" , "MO") )
    DBSession.add( State("Montana" , "MT") )
    DBSession.add( State("North Carolina" , "NC") )
    DBSession.add( State("North Dakota" , "ND") )
    DBSession.add( State("Nebraska" , "NE") )
    DBSession.add( State("New Hampshire" , "NH") )
    DBSession.add( State("New Jersey" , "NJ") )
    DBSession.add( State("New Mexico" , "NM") )
    DBSession.add( State("Nevada" , "NV") )
    DBSession.add( State("New York" , "NY") )
    DBSession.add( State("Ohio" , "OH") )
    DBSession.add( State("Oklahoma" , "OK") )
    DBSession.add( State("Oregon" , "OR") )
    DBSession.add( State("Pennsylvania" , "PA") )
    DBSession.add( State("Rhode Island" , "RI") )
    DBSession.add( State("South Carolina" , "SC") )
    DBSession.add( State("South Dakota" , "SD") )
    DBSession.add( State("Tennessee" , "TN") )
    DBSession.add( State("Texas" , "TX") )
    DBSession.add( State("Utah" , "UT") )
    DBSession.add( State("Virginia" , "VA") )
    DBSession.add( State("Vermont" , "VT") )
    DBSession.add( State("Washington" , "WA") )
    DBSession.add( State("Wisconsin" , "WI") )
    DBSession.add( State("West Virginia" , "WV") )
    DBSession.add( State("Wyoming" , "WY") )
    
    transaction.commit()
