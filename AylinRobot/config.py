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
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6055881643:AAHlHOq107K2L5y4UVgsXtAKx_3v9ulJuLo")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "ATOMultiBot")
   BOT_NAME = os.environ.get("BOT_NAME", "𓆩𝙰𝚃𝙾𓆪")
   OWNER_ID = int(os.environ.get("OWNER_ID","5591796078"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "ATOMultiBot") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001918131221"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "𓆩𝙰𝚃𝙾𓆪 𝑷𝒍𝒂𝒚𝑳𝒊𝒔𝒕")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001989468874"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1001918131221"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "4dc7aa73-cdde-448f-b267-5ee0a7285684")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "@ATOMultiBot")
   CHANNEL = os.environ.get("CHANNEL", "ATO_RESMl")
   SUPPORT = os.environ.get("SUPPORT", "kasbinxeyallari1")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/fe9dce4d50e2ee03d5894.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/fe9dce4d50e2ee03d5894.jpg")