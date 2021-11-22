# from pymongo import MongoClient
# # pprint library is used to make the output look more pretty
# from pprint import pprint
#
# # connect to MongoDB, change the << MONGODB URL >> to reflect
# #your own connection string
# client = MongoClient(<<MONGODB URL>>)
# db=client.admin
# # Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)
import pymongo
import ssl
from datetime import date
import pandas as pd

myclient = pymongo.MongoClient("mongodb+srv://afridi:afridi0153@cluster0.sbrek.mongodb.net/test",ssl_cert_reqs=ssl.CERT_NONE)
mydb = myclient["Bank_App"]

mycol = mydb["user"]

dict_keys = ["account_type","_id","nid","name","age","dob","address","contact","gender","hobby","entry_date"]
dict_values = ["Savings","111311111","111111111","ab","23"," ","xyz","1111111111","Male","travel",f"{date.today()}"]
dict=dict(zip(dict_keys,dict_values))
mycol.insert_one(dict)
print(mydb.list_collection_names())