from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

class Connection:
    engine = create_engine('postgresql://avnadmin:AVNS_K9LUif-9czu2_da41dT@pg-304e8d15-data-warehouse2579.i.aivencloud.com:14672/Data_Warehouse_Depression_Factor')

    # ✅ Use sessionmaker to create new session instances instead of a shared one
    SessionFactory = sessionmaker(bind=engine)

    @classmethod
    def get_session(cls):
        """Create a new session instance for every request to avoid concurrency issues."""
        return cls.SessionFactory()

    @classmethod
    def get_base(cls):
        """Automap the database schema."""
        Base = automap_base()
        Base.prepare(autoload_with=cls.engine)
        return Base