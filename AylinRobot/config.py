# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "23110135"))
   API_HASH = os.getenv("API_HASH", "ae975527472ab73d41eb7a771fa152fe")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6243129680:AAGwC3KZLvo5q7WI4q5-lGnOy_iW9JY3seY")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "RegionMusicRoBot")
   BOT_NAME = os.environ.get("BOT_NAME", "ATONezaret")
   OWNER_ID = int(os.environ.get("OWNER_ID","5637445914"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "Mirzeyev_645") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001886665096"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "DenemeKanal")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001886665096"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1001886665096"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "4dc7aa73-cdde-448f-b267-5ee0a7285684")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "ATO")
   CHANNEL = os.environ.get("CHANNEL", "HuseynH")
   SUPPORT = os.environ.get("SUPPORT", "HuseynH")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/7b01cef8f87059387d91b.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/7b01cef8f87059387d91b.jpg")