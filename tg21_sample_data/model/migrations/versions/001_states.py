from sqlalchemy import *
from migrate import *

metadata = MetaData(migrate_engine)

states_table = Table("state", metadata,
                    Column("id", Integer, primary_key=True),
                    Column("name", Text),
                    Column("postal_code", String(2))
                )


def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    states_table.create()

def downgrade():
    states_table.drop()
