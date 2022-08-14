import os
from dotenv import load_dotenv

import pymongo

load_dotenv()

class Pymongo:
    def __init__(self) -> None:
        MONGO_HOST = os.getenv("MONGO_HOST")
        MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
        MONGO_USERNAME = os.getenv("MONGO_USERNAME")
        self.client = pymongo.MongoClient(f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}{MONGO_HOST}",
            tls=True,
            tlsCAFile="isrgrootx1.pem",
            tlsAllowInvalidHostnames=True,
            retryWrites=False,)
        self.database = self.client[os.getenv("DATABASE_ENVIROMENT")]
        #self.database = self.client[os.getenv("DATABASE_ENVIROMENT")]['candidato']

# db = list(Pymongo().database.find())

# print(db)

# https://www.google.com/search?q=ac-lb5cmqd-shard-00-01.9s8u6au.mongodb.net%3A27017%3A+%5BSSL%3A+CERTIFICATE_VERIFY_FAILED%5D+certificate+verify+failed%3A+certificate+has&oq=ac-lb5cmqd-shard-00-01.9s8u6au.mongodb.net%3A27017%3A+%5BSSL%3A+CERTIFICATE_VERIFY_FAILED%5D+certificate+verify+failed%3A+certificate+has&aqs=chrome..69i57.647j0j7&sourceid=chrome&ie=UTF-8

# https://stackoverflow.com/questions/69397039/pymongo-ssl-certificate-verify-failed-certificate-has-expired-on-mongo-atlas

# https://www.mongodb.com/community/forums/t/keep-getting-serverselectiontimeouterror/126190
