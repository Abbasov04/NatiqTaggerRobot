import config
from helper.database.database import Database

db = Database(config.MONGODB_URI, config.SESSION_NAME)
