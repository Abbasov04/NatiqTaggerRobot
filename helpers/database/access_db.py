# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

from MusicAzBot.config import Config
from helpers.database.database import Database

db = Database(Config.MONGODB_URI, Config.BOT_USERNAME)
