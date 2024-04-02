#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from models.base_model import Base

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.user = os.environ.get('HBNB_MYSQL_USER')
        self.pwd = os.environ.get('HBNB_MYSQL_PWD')
        self.host = os.environ.get('HBNB_MYSQL_HOST')
        self.db = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(f"mysql+mysqldb://{self.user}:{self.pwd}@{self.host}/{self.db}", pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)