from tokenize import String
from typing import Generic

#class Pet(Generic[String s]):
from pymongo import common


class Pet(common.BaseObject, Generic):
    #class MongoClient(common.BaseObject, Generic[_DocumentType]):
    name = None

    def __init__(self, name):
        self.name = name
        print("hello from pet: " + name)

    @property
    def getName(self):
        print('getName')
        return self.name
