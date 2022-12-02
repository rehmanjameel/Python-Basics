from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connect with data_base
engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
# manage tables
base = declarative_base()


class Registration(base):

    __tablename__ = 'register'

    register_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)

    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username


base.metadata.create_all(engine)
