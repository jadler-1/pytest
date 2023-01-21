3333  # folks want me to comment more...fuck them...learn to read code
# import str
# import sys
from db.mongo_test import test_client
from domain.Pet import Pet
from util.util_test import json_test
import date.date_test
from enum import Enum
# import domain.Person
from domain import Person


class Test_Level(Enum):
    TEST1 = 1
    TEST2 = 2
    TEST3 = 3
    TEST4 = 4
    TEST5 = 5
    TEST6 = 6


test_type = Test_Level.TEST1

if test_type == Test_Level.TEST1:
    # if test_type == 1:
    test_client()

if test_type == Test_Level.TEST2:
    date.date_test.test()

if test_type == Test_Level.TEST3:
    # util.util_test.json_test()
    json_test()

if test_type == Test_Level.TEST4:
    Person.test()

if test_type == Test_Level.TEST5:
    p = Pet("ginger")
    print(p.getName)
    print(p)

print('end of file')
