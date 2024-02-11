import os
from .db_models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnector:
    def __init__(self, db_name):
        self.db_name = db_name
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', self.db_name))
        self.engine = create_engine(f"sqlite:///{db_path}")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def close_connection(self):
        self.session.close()
