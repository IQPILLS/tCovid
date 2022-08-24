def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/tCovid"
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    return client['tCovid']


if __name__ == "__main__":
    # Get the database
    dbname = get_database()
