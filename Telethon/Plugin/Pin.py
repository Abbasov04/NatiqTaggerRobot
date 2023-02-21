import logging, asyncio, random
from telethon import events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from AylinRobot.config import Config


@client.on(events.NewMessage(pattern="^.pin ?(.*)"))
async def pin(event):
    if event.sender_id == Config.OWNER_ID
        if not event.reply_to_msg_id:
            return await event.reply("🗨 Zəhmət Olmasa Bir Mesaja Yanıt Verin")
        await event.reply("📌 Sahibim Mesajınlz Pinləndi!")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply(f"Sən {BOT_NAME} Bota Sahib Deyilsən!\n⛔ Pinləməyə Çalışma.")
 

@client.on(events.NewMessage(pattern="^.unpin ?(.*)"))
async def unpin(event):
    if event.sender_id == Config.OWNER_ID
        if not event.reply_to_msg_id:
            return await event.reply("🗨 Zəhmət Olmasa Pinlənmiş Mesaja Yanıt Verin")
        await event.reply("Sahibim Pinlənmiş Mesaj Qaldırıldı")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply(f"Sən {BOT_NAME} Bota Sahib Deyilsən!\n⛔ UnPinləməyə Çalışma.")