# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import shutil, psutil, traceback, os, datetime, random, string, time, traceback, aiofiles, asyncio
from AylinRobot.translation import *
from AylinRobot.config import Config
from AylinRobot import AylinRobot as app
from pyrogram import Client as USER
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram.types import Message
from pyrogram import Client, filters, __version__
from pyrogram.errors import FloodWait

async def handle_user_status(app: Client, cmd: Message):
    chat_id = cmd.chat.id
    if not await db.is_user_exist






@app.on_message(filters.command(["stats"]) & filters.user(Config.OWNER_ID))
async def botstats(app: Client, message: Message):
    Aylin = await app.send_message(message.chat.id, LAN.STATS_STARTED.format(message.from_user.mention))
    all_users = await db.get_all_users()
    groups = 0
    pms = 0
    async for user in all_users:
        if str(user["id"]).startswith("-"):
            groups += 1
        else:
            pms += 1
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await Aylin.edit(text=LAN.STATS.format(Config.BOT_USERNAME, total_users, groups, pms, total, used, disk_usage, free, cpu_usage, ram_usage, __version__))


@app.on_message()
async def Aylin(app: Client, cmd: Message):
    await handle_user_status(app, cmd)


@app.on_message(filters.command("test") & filters.user(Config.OWNER_ID) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


