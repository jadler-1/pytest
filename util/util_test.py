import json


# print("util tests")


def json_test():
    print("json_test")
    x = '{ "name":"John", "age":30, "city":"New York"}'

    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["age"])

    res = __json_from_file()

    print(res)


def __json_from_file():
    f = None
    desc = None
    try:
        f = open("data/refData.txt", "r")
        j = f.read();
        print(j)
        y = json.loads(j)

        # the result is a Python dictionary:
        # desc = print(y["md"])
        desc = y["md"]
        print(desc)
    except Exception as e:
        print('Exception')
        print(e)
    except IOError as e:
        print('File not found')
        print(e)
    finally:
        if f is not None:
            f.close()

    return desc


def my_function(dict):
    try:
        print("His last name is " + dict["lname1"])
    except Exception as e:
        print('Exception')
        print(e.with_traceback(None))

    keys = dict.keys()
    for parm in keys:
        print(parm)


def lambda_test(x):
    lambda a: a + 10
    print(x(5))
