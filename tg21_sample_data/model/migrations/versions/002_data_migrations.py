from sqlalchemy import *
from migrate import *

metadata = MetaData(migrate_engine)

data_migration_table = Table("data_migration", metadata,
                    Column("id", Integer, primary_key=True),
                    Column("unique_code", Text, unique=True),
                    Column("date_created", DateTime)
                )

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    data_migration_table.create()

def downgrade():
    # Operations to reverse the above upgrade go here.
    data_migration_table.drop()
