#from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

# Get the URI from the environment
MONGO_URI =  os.getenv("MONGO_URI")


# Create the MongoClient
client = MongoClient(MONGO_URI)
users_db = client["Users"]





