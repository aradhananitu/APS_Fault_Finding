import pymongo
import pandas as pd

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME="APS"
Collection_Name="sensor"


if __name__=="_main_":
    df=pd.read_csv(data_file_path)
    print((f'Rows and Columns: {df.shape}'))

    #Convert dataframe to json format so that we can dump these record to mongoDB
    df.reset_index(drop=True,inplace=True)

    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json file to mongoDB
    client[DATABASE_NAME][COLLECTION].insert_many(json_record)



