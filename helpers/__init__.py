# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Satışa Qoyan Kimliyindən Aslı Olmayaraq Kankret Peysərdi


__version__ = "0.7.0"

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from AylinRobot.config import Config


MONGODB_CLI = MongoClient(Config.MONGODB_URI)
db = MONGODB_CLI.wbb
