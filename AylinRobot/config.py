# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi



import os

class Config:

   API_ID = int(os.getenv("API_ID", "8953338"))
   API_HASH = os.getenv("API_HASH", "fe21f223cb02d8f7c1cbda651f553a45")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "5636190781:AAEKrN6CzshWjiBLgHIOPkpD0Hk-tQDevu8")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "AylinRobot")
   OWNER_ID = int(os.environ.get("OWNER_ID","5865605067"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "HuseynH") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001886156935"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "AylinRobotPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001727904239"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1001820370604"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "05a017d5-e3e5-424d-941f-3e60645e3141")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "HUSEYN")
   CHANNEL = os.environ.get("CHANNEL", "HuseynH")
   SUPPORT = os.environ.get("SUPPORT", "HuseynH")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/e0332fa83406aa14ef0a1.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b2c2ed59a89933a384ae3.jpg")
   