import os
import re
import sys
import asyncio
import subprocess
from asyncio import sleep
from AylinRobot import AylinRobot as app
from pyrogram.types import Message
from helpers.filters import command
from pyrogram import Client, filters
from os import system, execle, environ
from AylinRobot.config import Config


@app.on_message(command(["restart"]) &(Config.OWNER_ID)& ~filters.edited)
async def restart_bot(_, message: Message):
    msg = await message.reply("`Botu yenidən başladın...`")
    args = [sys.executable, "AylinRobot"]
    await msg.edit("✅ bot yenidən işə salındı\n\n• indi bu botu yenidən istifadə edə bilərsiniz.")
    execle(sys.executable, *args, environ)
    return
