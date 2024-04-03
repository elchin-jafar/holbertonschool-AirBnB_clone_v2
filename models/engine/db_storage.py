#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None
    classes = {'User': User,
               'Place': Place,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Review': Review
               }

    def __init__(self):
        self.user = os.getenv('HBNB_MYSQL_USER')
        self.pwd = os.getenv('HBNB_MYSQL_PWD')
        self.host = os.getenv('HBNB_MYSQL_HOST')
        self.db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(self.user, self.pwd,
                                              self.host, self.db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        result = {}

        if cls:
            class_obj = self.classes.get(cls)
            if class_obj:
                for instance in self.__session.query(class_obj).all():
                    key = f"{cls}.{instance.id}"
                    result[key] = instance
        else:
            for class_name, class_obj in self.classes.items():
                for instance in self.__session.query(class_obj).all():
                    key = f"{class_name}.{instance.id}"
                    result[key] = instance
        return result
    
    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)