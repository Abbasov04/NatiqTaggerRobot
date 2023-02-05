# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from AylinRobot.config import Config
from AylinRobot.Plugin.Broadcast import Broadcast

db = Database(Config.MONGODB_URI, Config.BOT_USERNAME)
mongo_db_veritabani = MongoClient(Config.MONGODB_URI)
dcmdb = mongo_db_veritabani.handlers
MONGODB_CLI = MongoClient(Config.MONGODB_URI)
db = MONGODB_CLI.wbb