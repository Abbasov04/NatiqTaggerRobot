import os
from AylinRobot.translation import Translation
from AylinRobot.config import Config
from pyrogram import Client
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AylinRobot import AylinRobot as app

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum


import os
from AylinRobot.translation import Translation
from AylinRobot.config import Config
from pyrogram import Client
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AylinRobot import AylinRobot as app

@app.on_callback_query()
async def cb_data(client, message):
    if message.data == "home":
        await message.message.edit_text(
            text=Translation.START_TEXT.format(message.from_user.mention, Config.BOT_USERNAME),
            reply_markup=Translation.START_BUTTONS,
            disable_web_page_preview=True,
        )
    elif message.data == "help":
        await message.message.edit_text(
            text=Translation.HELP_TEXT.format(message.from_user.mention),
            reply_markup=Translation.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "musıc":
        await message.message.edit_text(
            text=Translation.MUSIC_TEXT,
            reply_markup=Translation.MUSIC_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "tg":
        await message.message.edit_text(
            text=Translation.TELEGRAPH_TEXT,
            reply_markup=Translation.TELEGRAPH_BUTTONS,
            disable_web_page_preview=True
        ) 
    elif message.data == "eylence":
        await message.message.edit_text(
            text=Translation.EYLENCE_TEXT,
            reply_markup=Translation.EYLENCE_BUTTONS,
            disable_web_page_preview=True
        )        
    elif message.data == "sehıd":
        await message.message.edit_text(
            text=Translation.SEHID_TEXT,
            reply_markup=Translation.SEHID_BUTTONS,
            disable_web_page_preview=True
        ) 
    elif message.data == "oyun":
        await message.message.edit_text(
            text=Translation.OYUN_TEXT,
            reply_markup=Translation.OYUN_BUTTONS,
            disable_web_page_preview=True
        )        
    elif message.data == "sahib":
        await message.message.edit_text(
            text=Translation.SAHIB_TEXT,
            reply_markup=Translation.SAHIB_BUTTONS,
            disable_web_page_preview=True
        ) 
    elif message.data == "elave":
        await message.message.edit_text(
            text=Translation.ELAVELER_TEXT.format(message.from_user.mention),
            reply_markup=Translation.ELAVE_BUTTONS,
            disable_web_page_preview=True
        ) 
    elif message.data == "refreshme":
        if config.UPDATES_CHANNEL:
            invite_link = await client.create_chat_invite_link(int(config.UPDATES_CHANNEL))
            try:
                user = await client.get_chat_member(int(config.UPDATES_CHANNEL), message.message.chat.id)
                if user.status == "kicked":
                    await message.message.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/leosupportx).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await message.message.edit(
                    text="<b>Hey</b> {},\n\n<b>You still didn't join our Updates Channel ☹️ \nPlease Join and hit on the 'Refresh 🔄' Button</b>".format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Our Updates Channel 🗣", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("Refresh 🔄", callback_data="refreshme")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await message.message.edit(
                    text="Something went Wrong. Contact my [Support Group](https://t.me/leosupportx).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        await message.message.edit(
            text=Translation.START_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=Translation.START_BUTTONS,
        )
    else:
        await message.message.delete()
