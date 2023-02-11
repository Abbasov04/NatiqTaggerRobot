# t.me/RoBotlarimTg | YouTube: RoBotlarimTg | t.me/EdaletSup
# t.me/aykhan_s | t.me/edalet_22
# GitHub: EdaletRoBot
from telethon import events
from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsAdmins
import random
from Config import Config 


edalet = TelegramClient('edalet', API_ID, API_HASH).start(bot_token=bot_token)

SAHIB = 586648198

@edalet.on(events.NewMessage(pattern="^/pin$"))
async def pin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("Bir mesajı cavablayın")
        await event.reply("Pinləndi")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply("Sən sahib deyilsən pinləməyə çalışma")

@edalet.on(events.NewMessage(pattern="^/unpin$"))
async def unpin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("Bir pinlənən mesajı cavablayın")
        await event.reply("Unpinləndi")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply("Sən sahib deyilsən unpinləməyə çalışma")



print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
edalet.run_until_disconnected()
