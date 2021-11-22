import pymongo
import ssl
from datetime import date
import pandas as pd

myclient = pymongo.MongoClient("mongodb+srv://afridi:afridi0153@cluster0.sbrek.mongodb.net/test",ssl_cert_reqs=ssl.CERT_NONE)
mydb = myclient["Bank_App"]

mycol = mydb["user"]

myquery = { "nid": input("Enter nid you want to update") }
newvalues = { "$set": { "contact": 2222222222 } }

mycol.update_one(myquery, newvalues)