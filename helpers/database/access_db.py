# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

from AylinRobot.config import Config
from helpers.database.database import Database
from AylinRobot.Plugin import Broadcast

db = Database(Config.MONGODB_URI, Config.BOT_USERNAME)
mongo_db_veritabani = MongoClient(Config.MONGODB_URI)
dcmdb = mongo_db_veritabani.handlers
