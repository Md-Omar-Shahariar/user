import pymongo
import ssl
from datetime import date
import pandas as pd

myclient = pymongo.MongoClient("mongodb+srv://afridi:afridi0153@cluster0.sbrek.mongodb.net/test",ssl_cert_reqs=ssl.CERT_NONE)
mydb = myclient["Bank_App"]

mycol = mydb["user"]
doc = mycol.find()
doc = pd.DataFrame(doc)
doc.pop("_id")
doc.to_csv("doc.csv",index=False)