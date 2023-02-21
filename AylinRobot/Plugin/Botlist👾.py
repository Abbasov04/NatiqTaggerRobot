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
import os
import asyncio
from pyrogram import ChatMemberStatus
from pyrogram.errors import FloodWait



@app.on_message(filters.command(["alist"]))
async def admins(client, message):
  try: 
    adminList = []
    ownerList = []
    async for admin in app.iter_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      if admin.privileges.is_anonymous == False:
        if admin.user.is_bot == True:
          pass
        elif admin.status == ChatMemberStatus.OWNER:
          ownerList.append(admin.user)
        else:  
          adminList.append(admin.user)
      else:
        pass   
    lenAdminList= len(ownerList) + len(adminList)  
    text2 = f"{message.chat.title}** Qrupundakı Adminlərin Siyahısı**\n\n"
    try:
      owner = ownerList[0]
      if owner.username == None:
        text2 += f"👑 Sahib\n└ {owner.mention}\n\n👮🏻 Adminlər\n"
      else:
        text2 += f"👑 Sahib\n└ @{owner.username}\n\n👮🏻 Adminlər\n"
    except:
      text2 += f"👑 Sahib\n└ <i>Hidden</i>\n\n👮🏻 Adminlər\n"
    if len(adminList) == 0:
      text2 += "└ <i>Adminlər gizlidir</i>"  
      await app.send_message(message.chat.id, text2)   
    else:  
      while len(adminList) > 1:
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"├ ❤️ {admin.mention}\n"
        else:
          text2 += f"├ ❤️ @{admin.username}\n"    
      else:    
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"└ ❤️ {admin.mention}\n\n"
        else:
          text2 += f"└ ❤️ @{admin.username}\n\n"
      text2 += f"✅ | **İdarəçilərin ümumi sayı**: {lenAdminList}\n❌ | Botlar və gizli adminlər rədd edildi."  
      await app.send_message(message.chat.id, text2)           
  except FloodWait as e:
    await asyncio.sleep(e.value)       

@app.on_message(filters.command("bots"))
async def bots(client, message):  
  try:    
    botList = []
    async for bot in app.iter_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bot.user)
    lenBotList = len(botList) 
    text3  = f"`{message.chat.title}`**Qrupundakı Botlar**\n💁‍♀️ **Axtarış Edən** {message.from_user.mention}\n\n@{Config.BOT_USERNAME} **Sizin Üçün Botların Siyahısın Gətirdi**\n\n"
    while len(botList) > 1:
      bot = botList.pop(0)
      text3 += f"├ 🔮 @{bot.username}\n"    
    else:    
      bot = botList.pop(0)
      text3 += f"└ 🔮 @{bot.username}\n\n"
      text3 += f"**✅ Botların Ümumi Sayı**: {lenBotList}"  
      await app.send_message(message.chat.id, text3)
  except FloodWait as e:
    await asyncio.sleep(e.value)