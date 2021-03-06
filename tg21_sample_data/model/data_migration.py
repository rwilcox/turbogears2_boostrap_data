#autogenerated by sqlautocode

from datetime import datetime
import sys
import os

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from tg21_sample_data.model import DeclarativeBase, metadata, DBSession
import transaction

class DataMigration(DeclarativeBase):
    __tablename__ = 'data_migration'
    
    #column definitions
    date_created = Column(u'date_created', DateTime(timezone=False))
    id = Column(u'id', Integer(), primary_key=True, nullable=False)
    unique_code = Column(u'unique_code', Text(length=None, convert_unicode=False, assert_unicode=None), unique=True)
    
    #relation definitions
    
    
    # methods
    def __init__(self, unique_code):
        self.unique_code = unique_code
        self.date_created = datetime.now()
    
    
    def migration_needs_to_run(self):
        return DBSession.query(DataMigration).filter_by(unique_code = self.unique_code).count() == 0
    
    
    @classmethod
    def run_all(cls, conf):
        top_module_name = conf['package_name']   # You need to create this, thank you. WD-rpw 03-10-2010
        mod = __import__(top_module_name + ".websetup.bootstrap_data", fromlist=[top_module_name, "websetup"])
        for modname in dir(mod):
            if modname.startswith("bootstrap"):
                fully_qualified_mod_name = "%s.websetup.bootstrap_data.%s" % (top_module_name, modname)
                dmigration = DataMigration(fully_qualified_mod_name)
                if dmigration.migration_needs_to_run():
                    mod = sys.modules[ fully_qualified_mod_name ]
                    mod.upgrade(conf)
                    DBSession.add(dmigration)
        transaction.commit()
        

