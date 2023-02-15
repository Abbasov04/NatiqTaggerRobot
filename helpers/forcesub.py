# © Naviya2

import asyncio
from AylinRobot.config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(app: Client, event: Message):

    try:
        invite_link = await app.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL)))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(app, event)
        return fix_
    except Exception as err:
        print(f"{Config.UPDATES_CHANNEL} kanalına məcburi abunə olmaq mümkün deyil\n\nXəta: {err}\n\nDəstək Qrupu ilə əlaqə saxlayın: @{Config.CHANNEL}")
        return 200
    try:
        user = await app.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL)), user_id=event.from_user.id)
        if user.status == "kicked":
            await app.send_message(
                chat_id=event.from_user.id,
                text=f"Üzr istəyirik, əzizim, məndən istifadə etmək qadağandır ☹️\nDəstək Qrupumuzda @{Config.CHANNEL} bildirməkdən çəkinməyin..",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=event.message_id
            )
            return 400
        else:
            return 200
    except UserNotParticipant:
        await app.send_message(
            chat_id=event.from_user.id,
            text="<b>Salam {} 👋\n\nYeniləmələr Kanalımıza abunə olana qədər məndən istifadə edə bilməzsiniz ☹️\n\nOdur ki, aşağıdakı düymə ilə Yeniləmələr Kanalımıza qoşulun və 'Yenilə 🔄' düyməsini sıxın 😊</b>".format(event.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("👨‍💻 Yeniliklər Kanalı", url=invite_link.invite_link)
                    ],

                    [   
                        InlineKeyboardButton("Yenilə 🔄", callback_data="refreshme")
                    ],
                ]
            ),
            parse_mode="HTML",
            reply_to_message_id=event.message_id
        )
        return 400
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Nə isə səhv getdi!  Məcburi Abunə olmaq mümkün deyil.\nXəta: {err}\n\nDəstək Qrupu ilə əlaqə saxlayın: @{Config.CHANNEL}")
        return 200
