import random, os
from random import choice
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters


banned_users = [-1001600046749]

@app.on_message(filters.command('ban') & filters.private)
async def ban_user(client, message):
    user_id = message.from_user.id
    if user_id not in banned_users:
        banned_users.append(user_id)
        await message.reply(f'User {user_id} Qrupdan Banlandınız Zəhmət olmasa hərəkətlərivizə fikir verin')

@app.on_message(filters.command('unban') & filters.private)
async def unban_user(client, message):
    user_id = message.from_user.id
    if user_id in banned_users:
        banned_users.remove(user_id)
        await message.reply(f'User {user_id} Banı Açıldı')

@app.on_message(filters.private)
async def handle_private_message(client, message):
    user_id = message.from_user.id
    if user_id in banned_users:
        await client.kick_chat_member(message.chat.id, user_id)
        await message.reply(f'User {user_id} Qrupdan Banlandınız Zəhmət olmasa hərəkətlərivizə fikir verin')