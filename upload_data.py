from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://anurajput564:anurajput564@cluster0.bb3fzpu.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

# Create database name and collection name
DATABASE_NAME = "mlproject"
COLLECTION_NAME = 'waferfault'

#read data as a dataframe 
df = pd.read_csv("Z:\MLproject\Sensor_Project\notebooks\wafer_23012020_041211.csv")
df = df.drop("Unnamed: 0",axis=1)

#Convert the data into json
json_record = list(json.loads(df.T.to_json()).values())


#now dump the data into database
client[DATABASE_NAME][COLLECTION_NAME].update_many(json_record)
