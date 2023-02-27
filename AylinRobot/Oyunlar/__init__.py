# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

from os.path import dirname, basename, isfile, join
import glob
from time import sleep
from pyrogram import Client
import logging
from AylinRobot.config import Config

# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")
]

if Config.OWNER_ID and len(Config.OWNER_ID) and Config.OWNER_ID.isdigit():
    Config.OWNER_ID = int(Config.OWNER_ID)  # type: ignore
else:
    OWNER_ID = None  # type: ignore


# Oyun Verileri
oyun = {}  # type: ignore

# rating
rating = {}  # type: ignore
