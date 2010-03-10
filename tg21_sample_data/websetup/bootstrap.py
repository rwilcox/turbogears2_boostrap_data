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
