import pymongo


def test_client():

    print("creating client")

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    #myclient = pymongo.MongoClient("mongodb://73.135.120.94/32")

    #myclient = pymongo.MongoClient("mongodb://73.135.120.94:27017/")

    #myclient = pymongo.MongoClient(
   #     "mongodb+srv://admin:admin@cluster0.gsusa.mongodb.net/?retryWrites=true&w=majority")

    print(myclient)
    print(type(myclient))

    myclient.close()

    if 1==1:
        return

    mydb = myclient.test

    print(myclient)

    mydb = myclient['mydatabase']

    mycol = mydb["customers"]

    mydict = {"name": "John", "address": "Highway 37"}

    x = mycol.insert_one(mydict)

    print(x.inserted_id)

    print(mydb.list_collection_names())

    #session = myclient.start_session()

    #mydb = myclient["mydatabase"]

    dblist = myclient.list_database_names()
    for db in dblist:
        print("database: " + db)
"""
    if "mydatabase" in dblist:
        print("The database exists.")
    else:
        print(f"The database {mydb} does not exists.")

    # print(mydb.)

    print(myclient.list_database_names())

    host_info = myclient['HOST']
    print("\nhost:", host_info)"""
