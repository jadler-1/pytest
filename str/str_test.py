#print("string tests")


def strLen(s):
    print('in sub module ass...')
    n = len(s)

    if n != 6:
        # print(f'The length {n} is 6')
        print("The length of " + s + " is not 6, " + "it is " + str(n))
    else:
        # print(f'{n} is not ideal!')
        # print(n + " is not ideal!")
        # s = (str(n) + " is not 6")
        s = "The length of " + s + " is 6"
        print(s)
