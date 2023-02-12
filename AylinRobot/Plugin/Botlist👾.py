# @AylinRobot
#@MusicAzBot
# Repo Açığdısa İcazəsis Götürmə Oğlum

import time
from asyncio import sleep
from time import time
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from AylinRobot.config import Config
from pyrogram import Client, filters

from pyrogram.types import Message
import os
import asyncio
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus

@app.on_message(filters.command('list') & filters.group)
async def start(client, msj):
    BOTLAR = []
    chat_id = msj.chat.id
    async for members in app.iter_chat_members(chat_id):
        botmu = members.user.is_bot
        if botmu == True:
            BOTLAR.append(members.user.mention)
            botlarsiyahi = '\n'.join(BOTLAR)
        else:
            pass

    botlarsiyahi = '\n'.join(BOTLAR)
    await client.send_message(chat_id, botlarsiyahi)
    
    
@app.on_message(filters.command(["remove","clean"]))
async def remove(client, message):
  global stopProcess
  try: 
    try:
      sender = await teletips.iter_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      bot = await teletips.iter_chat_member(message.chat.id, "self")
      if bot.status == ChatMemberStatus.MEMBER:
        await message.reply("🕹 | I need admin permissions to remove deleted accounts.")  
      else:  
        if len(chatQueue) > 5 :
          await message.reply("⛔️ | I'm already working on my maximum number of 5 chats at the moment. Please try again shortly.")
        else:  
          if message.chat.id in chatQueue:
            await message.reply("🚫 | There's already an ongoing process in this chat. Please /stop to start a new one.")
          else:  
            chatQueue.append(message.chat.id)  
            deletedList = []
            async for member in teletips.get_chat_members(message.chat.id):
              if member.user.is_deleted == True:
                deletedList.append(member.user)
              else:
                pass
            lenDeletedList = len(deletedList)  
            if lenDeletedList == 0:
              await message.reply("👻 | No deleted accounts in this chat.")
              chatQueue.remove(message.chat.id)
            else:
              k = 0
              processTime = lenDeletedList*10
              temp = await teletips.send_message(message.chat.id, f"🚨 | Total of {lenDeletedList} deleted accounts has been detected.\n⏳ | Estimated time: {processTime} seconds from now.")
              if stopProcess: stopProcess = False
              while len(deletedList) > 0 and not stopProcess:   
                deletedAccount = deletedList.pop(0)
                try:
                  await teletips.ban_chat_member(message.chat.id, deletedAccount.id)
                except Exception:
                  pass  
                k+=1
                await asyncio.sleep(10)
              if k == lenDeletedList:  
                await message.reply(f"✅ | Successfully removed all deleted accounts from this chat.")  
                await temp.delete()
              else:
                await message.reply(f"✅ | Successfully removed {k} deleted accounts from this chat.")  
                await temp.delete()  
              chatQueue.remove(message.chat.id)
    else:
      await message.reply("👮🏻 | Sorry, only admins can execute this command.")  
  except FloodWait as e:
    await asyncio.sleep(e.value)