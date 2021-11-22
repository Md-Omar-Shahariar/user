import pymongo
import ssl


myclient = pymongo.MongoClient("mongodb+srv://afridi:afridi0153@cluster0.sbrek.mongodb.net/test",ssl_cert_reqs=ssl.CERT_NONE)
mydb = myclient["Bank_App"]

mycol = mydb["user"]
myquery = { "_id": input("Enter Nid to delete") }

mycol.delete_one(myquery)