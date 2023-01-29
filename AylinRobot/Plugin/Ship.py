import os
import time
import psutil
import shutil
import string
import asyncio
from random import choice
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import idle, filters
from pyrogram import Client, filters

import random


@app.on_message(pyrogram.Filters.command(["ship"]))
def ship(client, message):
    chat_members = client.get_chat_members(chat_id=message.chat.id)
    members = [member.user.first_name for member in chat_members]
    two_random_members = random.sample(members, 2)
    client.send_message(
        chat_id=message.chat.id,
        text=f"Randomly selected members: {two_random_members[0]} and {two_random_members[1]}"
    )