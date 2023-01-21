class Person:
    name = 'joe blow'
    age = 21

    def __init__(self, n, a):
        Person.name = n
        age = a


def test():
    print(Person.name)
    print(Person.age)
    p1 = Person("John", 36)
    print(p1.name)
    print(p1.age)

    print()
