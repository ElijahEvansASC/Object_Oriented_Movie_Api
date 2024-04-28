from pymongo import MongoClient

class GVars:
    def __init__(self):
        self.connection_string = "mongodb://student:alfred@10.33.86.229:8006"
        self.db_name = "MovieDatabase"
        self.movie_collection_name = "Movies"

        def connect_to_mongo_db(db_name, connection_string):
            client = MongoClient(connection_string)
            db = client.get_database(db_name)
            return db