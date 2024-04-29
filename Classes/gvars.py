from pymongo import MongoClient

class GVars:
    def __init__(self):
        self.connection_string = "mongodb://student:alfred@10.33.86.229:27017"
        self.db_name = "MovieDatabase"
        self.collection_name = "MovieData"

    def connect_to_mongo_db(self):
        client = MongoClient(self.connection_string)
        db = client.get_database(self.db_name)
        return db