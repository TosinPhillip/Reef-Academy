#from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
import dotenv


# Load environment variables
dotenv.load_dotenv()

# Get the URI from the environment
MONGO_URI = dotenv.get_key(dotenv_path=dotenv.find_dotenv(), key_to_get='MONGO_URI')


# Create the MongoClient
client = MongoClient(MONGO_URI)
user_db = client["Users"]



# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# collection = db["test_collection"]



