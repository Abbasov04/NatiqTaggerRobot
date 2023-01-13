__version__ = "0.7.0"

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from MusicAzBot.config import Config


MONGODB_CLI = MongoClient(Config.MONGODB_URI)
db = MONGODB_CLI.wbb
