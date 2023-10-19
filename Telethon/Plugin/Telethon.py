## Sahib HuseynH Satış Qadağandır

import logging, asyncio, random
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from AylinRobot.config import Config
from Telethon.Mesajlar import soz,  emoji, bayrag
From Telethon import Button

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)
 
api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []
 
ozel_list = [2074934667]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}
	
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 

@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
	
@client.on(events.NewMessage(pattern="^.tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/tag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")


@client.on(events.NewMessage(pattern="^.ttag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("*❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("** ⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
 
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("***🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver!**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/ttag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Uğurla Başladıldl.!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n📢 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n📢 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
 
 
 
@client.on(events.NewMessage(pattern="^.stag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("*❌ PM Də Tağ Olmaz**\n✅ Bu Əmr Sadəcə Qruplar Və Kanllar Üçün Keçərlidir.")
  
  admins = []
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("⛔ **Siz Admin Deyilsiz!**\n✅ **Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
 
  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("ℹ **Köhnə Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Bir Mesajı Yanıtlayın Yada Tağ Edə Bilməyim Üçün Bir Səbəb Yazın\n✔ Misal Üçün:-`/etag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ Prosesi Başladıldı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅  Tağ Prosesi Uğurla Tamamlandı**\n\n**📊 Tağ Edilınlərin Sayı:-**  `{rxyzdev_tagTot[event.chat_id]}`\n**👤 Prosesi Başladan:-** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla tamamlandı**\n\n**⚡ Tağ Edildi:-**  `{rxyzdev_tagTot[event.chat_id]}`\n**🗣 Prosesi Başladan:-**  {rxyzdev_initT}")
 
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern="^.etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/etag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"- [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f" - [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 


@client.on(events.NewMessage(pattern="^.rtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/rtag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
 

@client.on(events.NewMessage(pattern="^.btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/btag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"- [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f" - [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
		


@client.on(events.NewMessage(pattern="^.admin ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "♕︎ Qrup Adminlərinin Siyahısı ♕︎\n\n"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n ➪ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation
    
    
    
    
SAHIB = Config.OWNER_ID

@client.on(events.NewMessage(pattern="^.pin ?(.*)"))
async def pin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("🗨 Zəhmət Olmasa Bir Mesaja Yanıt Verin")
        await event.reply("📌 Sahibim Mesajınlz Pinləndi!")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} Bota Sahib Deyilsən!\n⛔ Pinləməyə Çalışma.")
 

@client.on(events.NewMessage(pattern="^.unpin ?(.*)"))
async def unpin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("🗨 Zəhmət Olmasa Pinlənmiş Mesaja Yanıt Verin")
        await event.reply("Sahibim Pinlənmiş Mesaj Qaldırıldı")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} Bota Sahib Deyilsən!\n⛔ UnPinləməyə Çalışma.")    
        





@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))


userjoin = (

    "Salam axır ki gəlib çıxdın sənin yoluvu çoxdandı gözləyirdik.👀 bizimlə xoş zaman keçirəcəynə əmin ola bilərsən🥳",
    "Salam Siz öz dəyərli vaxtınızı daha da əyləncəli və maraqlı keçirmək üçün doğru ünvandasınız🎯. Aramızda sizi görmək çox xoş oldu bizə🤗 xoş Gəldiz😊",
)




@client.on(events.NewMessage(pattern=f'@Mirzeyev_645'))
@client.on(events.NewMessage(pattern='Kənan'))
@client.on(events.NewMessage(pattern='@Yoxduburda'))
@client.on(events.NewMessage(pattern='Həsən'))
async def handler(event):
    await event.reply(random.choice(Aylin))



Aylin = (
    "😒 Sahibim Burda Yoxdu Gələndə Yazar",
    "🤭 Hmm Mənim Sahibimlə Nə İşin Var?",
    "😖 Aktif deil gələndə yazacağ",
    "Burda olmasada qəlbi sizinlədi ❤️",
)




SOYUS_CAVAB = ["🤖 Mən Mesajı Sildim\n\n⛔ SƏBƏB:- Söyüş Tipli Sözlər isdifadə Elıdiyin Üçün","🚫 Söyüş Tipli Mətn Olduğu Üçün Yazılan Mesajı Sildim"]


@client.on(events.NewMessage(pattern=f'(?i)s[iı]k+'))
@client.on(events.NewMessage(pattern=f'(?i)pox+'))
@client.on(events.NewMessage(pattern=f'(?i)s[iı]kd[iı]+'))
@client.on(events.NewMessage(pattern=f'(?i)da[sş]ax+'))
@client.on(events.NewMessage(pattern=f'(?i)s[iı]k[iı]m+'))
@client.on(events.NewMessage(pattern=f'(?i)p[eə]ys[eə]r+'))
@client.on(events.NewMessage(pattern=f'(?i)g[iı]jdlaa[ghx]+'))
@client.on(events.NewMessage(pattern=f'(?i)s[iı]k[iı]lm[iı][şs]+'))
@client.on(events.NewMessage(pattern=f'(?i)c[ıi]nd[ıi]r+'))
@client.on(events.NewMessage(pattern=f'(?i)q[əe]hb[əe]+'))
@client.on(events.NewMessage(pattern=f'(?i)dalbayov+'))
@client.on(events.NewMessage(pattern=f'(?i)c[ıi]r+'))
@client.on(events.NewMessage(pattern=f'(?i)xiyar+'))
@client.on(events.NewMessage(pattern=f'(?i)got+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.delete()
    await event.reply(f"{random.choice(SOYUS_CAVAB)}")



from telethon import events
import time

from telethon import events, errors
from telethon.tl.types import ChannelParticipantsAdmins
import time
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsAdmins


@client.on(events.NewMessage(incoming=True, pattern="^[!/]purge$"))
async def purge_messages(event):
    start = time.perf_counter()
    if event.is_private:
        await event.respond("Bu əmri yalnız qruplarda icra edə bilərsiniz.", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.respond("Bu əmri yalnız qrup yönəticiləri icra edə bilər.", parse_mode='markdown')
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.respond("Silməyə başlayacağım mesaja yanıt ver.")
        return

    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"✅ Təmizləmə prosesi {time_:0.2f} saniyədə tamamlandı"
    await event.respond(text, parse_mode='markdown')


async def is_group_admin(event):
    """
    Checks if the user is a group admin
    """
    try:
        user = await event.client.get_entity(event.input_chat)
        user_info = await event.client.get_participants(user, filter=ChannelParticipantsAdmins, limit=100)
        for u in user_info:
            if u.id == event.sender_id:
                return True
    except errors.rpcerrorlist.ChatAdminRequiredError:
        pass
    return False



import asyncio
import random
from telethon import events

faiz = ['10%','11%','12%','13%','14%','15%','16%','17%','18%','19%','20%','21%','22%','23%','24%','25%','26%','27%','28%','29%','30%','31%','32%','33%','34%','35%','36%','37%','38%','39%','40%','41%','42%','43%','44%','45%','46%','47%','48%','49%','50%','51%','52%','53%','54%','55%','56%','57%','58%','59%','60%','61%','62%','63%','64%','65%','66%','67%','68%','69%','70%','71%','72%','73%','74%','75%','76%','77%','78%','79%','80%','81%','82%','83%','84%','85%','86%','87%','88%','89%','90%','91%','92%','93%','94%','95%','96%','97%','98%','99%','100%']
urek = ['❤️','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❤️‍🔥','❤️‍🩹','❣️','💕','💞','💓','💗','💖','💘','💝']


@client.on(events.NewMessage(pattern="^/eros ?(.*)|^/ship ?(.*)"))
async def eros(event):
     if event.is_private:
          return await event.respond("Bu əmr qruplar üçün etibarlıdır!  ")
     qrup = await event.get_chat() 
     istifadeciler = await client.get_participants(qrup)
     sev1, sev2 = random.sample(istifadeciler, 2)
     secirem = await event.reply(f"{random.choice(urek)} Erosun oxu atıldı 🏹 \n🙈 Cütlükləri seçirəm")
     await asyncio.sleep(2)
     await secirem.delete()
     await event.reply(f"{random.choice(urek)} Cütlüklər:\n"
                       f" [{sev1.first_name}](tg://user?id={sev1.id})" + f" [{sev2.first_name}](tg://user?id={sev2.id})\n"
                       f"♥️ Sevgi Faizi: {random.choice(faiz)}")


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"🙋🏻 Salam mən qrupunuzdakı bütün üzvləri tağ edə bilərəm\n\n💁🏻 Ətraflı məlumat üçün Əmrlər bölməsinə daxil olun", button=(
                     [Button.url('➕ Qrupa Əlavə Et ➕','http://t.me/ATO_Tagger_Bot?startgroup=a')],
               [Button.inline(f"📚 Əmrlər", data="help"),
                Button.inline(f"👑 Sahib Əmrləri", data="reklam")],
               [Button.url('📢 Kanal', 'https://t.me/ATO_RESMl'),
                      Button.url('👨🏻‍💻 Bot Sahibi', 'https://t.me/Yoxduburda')],
                    ),
                    link_preview=False)


  if event.is_group:
    return await edalet.send_message(event.chat_id, f"Botun istifadə qaydasını öyrənmək üçün bota keçin", buttons=(
                     [Button.url('🤖 Bota Keç','https://t.me/ATO_Tagger_Bot?start=start')],
               [Button.url('📢 Kanal', 'https://t.me/ATO_RESMl'),
          Button.url('👨🏻‍💻 Bot Sahibi', 'https://t.me/Yoxduburda')],
                    ),
                    link_preview=False)



@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"🙋🏻 Salam mən qrupunuzdakı bütün üzvləri tağ edə bilərəm\n\n💁🏻 Ətraflı məlumat üçün Əmrlər bölməsinə daxil olun", button=(
                     [button.url('➕ Qrupa Əlavə Et ➕','http://t.me/ATO_Tagger_Bot?startgroup=a')],
               [Button.inline(f"📚 Əmrlər", data="help"),
                Button.inline(f"👑 Sahib Əmrləri", data="reklam")],
               [Button.url('📢 Kanal', 'https://t.me/ATO_RESMl'),
                      Button.url('👨🏻‍💻 Bot Sahibi', 'https://t.me/Yoxduburda')],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):  
    await event.edit(f"🕹 İstifadə: /ato\n📜 Açıqlama: Maraqlı sözlər ilə tağ edər\n\n🕹 İstifadə: /tag\n📜 Açıqlama: 5 nəfərlik tağ edər\n\n🕹 İstifadə: /etag\n📜 Açıqlama: Emoji ilə tağ edər\n\n🕹 İstifadə: /btag\n📜 Açıqlama: bayraqlar ilə tağ edər\n\n🕹 İstifadə: /ftag\n📜 Açıqlama: Məşhur futbolçuların adları ilə tağ edər\n\n🕹 İstifadə: /mafia\n📜 Açıqlama: Mafia rolları ilə tağ edər\n\n🕹 İstifadə: /adtag\n📜 Açıqlama: Maraqlı adlar ilə tağ edər\n\n🕹 İstifadə: /admins\n📜 Açıqlama: Qrup adminləri tağ edər\n\n🕹 İstifadə: /cancel\n📜 Açıqlama: Tağ prosesi dayandırar\n\n🕹 İstifadə: /ship\n📜 Açıqlama: Qrupda cütlük seçər\n\n🕹 İstifadə: /banda\n📜 Açıqlama: Qrupda silinən hesabları çıxardar\n\n🕹 İstifadə: /id\n📜 Açıqlama: ID atar", buttons=(
               [Button.url('📢 Kanal', 'https://t.me/ATO_RESMl'),
                      Button.url('🇦🇿 Reklam', 'https://t.me/ATO_RESMl')],
               [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="reklam"))
async def handler(event):  
    await event.edit(f"🔮 İstifadə: /stats\n📃 Açıqlama: Botun məlumatları göstərir\n\n🔮 İstifadə: /reklam\n📃 Açıqlama: Yayım etmək\n\n🔮 İstifadə: /block\n📃 Açıqlama: İstifadəçi blok etmək\n\n🔮 İstifadə: /unblock\n📃 Açıqlama: İstifadəçi bloku qaldırmaq\n\n🔮 İstifadə: /blocklist\n📃 Açıqlama: Blok siyahısı göstərir\n\n🔮 İstifadə: /delcmd\n📃 Açıqlama: (on - off) - Komanda silmə funksiyası", buttons=(
         [Button.url('👨🏻‍💻 Bot Sahibi', 'https://t.me/Yoxduburda')],
               [Button.url('📢 Kanal', 'https://t.me/ATO_RESMl'),
                      Button.url('🇦🇿 Reklam', 'https://t.me/ATO_RESMl')],
               [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)