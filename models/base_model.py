#!/usr/bin/python3
""" defines all common attributes/methods for other classes  """

from datetime import datetime
import models
import uuid


class BaseModel:
    """ This is BaseModel class that is main one  """

    def __init__(self, *args, **kwargs):
        """Constructor of BaseModel class"""
        if len(kwargs) != 0:
            for A, B in kwargs.items():
                if A == "__class__":
                    continue
                elif A == "updated_at":
                    self.updated_at = datetime.fromisoformat(B)
                elif A == "created_at":
                    self.created_at = datetime.fromisoformat(B)
                else:
                    setattr(self, A, B)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.st.new(self)

    def __str__(self):
        """ str dunder method, when print BaseModel """
        return "[{}] {} {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """ Save method, it updates time and save it into storage """
        self.updated_at = datetime.now()
        models.st.save()

    def to_dict(self):
        """It returns a dictionary"""
        prop = self.__dict__.copy()
        prop["__class__"] = self.__class__.__name__
        prop["created_at"] = self.created_at.isoformat()
        prop["updated_at"] = self.updated_at.isoformat()
        return prop
