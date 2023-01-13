from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} 👋

I'm Leo Song Downloader Bot 🇱🇰

You can download any song within a shortime with this Bot 🙂

If you want to know how to use this bot just
touch on " Help 🆘 "  Button 😊

Leo Projects 🇱🇰 
"""    
    HELP_TEXT = """
Hello {}👋

You should know following instructions to download songs 😊

You can download song by,

🔰<code>/song <song name></code>: Download songs from all sources
Ex : <code>/song alone</code>

Or,

🔰 via youtube URL s... Send me any Youtube URL to download it 😊
"""
    ABOUT_TEXT = """
🔰 **Bot :** [Leo Song Downloader Bot 🇱🇰](https://t.me/leosongdownloaderbot)
🔰 **Developer :** [Naviya 🇱🇰](https://telegram.me/naviya2)
🔰 **Updates Channel :** [Leo Updates 🇱🇰](https://telegram.me/new_ehi)
🔰 **Support Group :** [Leo Support 🇱🇰](https://telegram.me/leosupportx)
🔰 **Language :** [Python3](https://python.org)
🔰 **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
🔰 **Server :** [VPS](https://www.digitalocean.com)
"""

    ABOUT_DEV_TEXT = """
<b>Developer is a Super Noob 😅

You can find him in telegram as @naviya2 🇱🇰

Developer's github account : [Github](https://github.com/Naviya2) 🇱🇰

If you find any error on this bot please be kind to tell [Developer](https://t.me/naviya2) or in our [Support Group](https://t.me/leosupportx) 😊</b>
"""
    INFO_TEXT = """
Hey {mention},

Your details are here 😊

🔰 **First Name :** `{first_name}`
🔰 **Last Name  :** `{last_name}`
🔰 **Username   :** @{username}
🔰 **User Id    :** `{user_id}`
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Developer🧑‍💻', url='https://telegram.me/naviya2'),
        InlineKeyboardButton('Rate us ★', url='https://t.me/tlgrmcbot?start=leosongdownloaderbot-review')
        ],[
        InlineKeyboardButton('Updates Channel🗣', url='https://t.me/new_ehi'),
        InlineKeyboardButton('Support Group 👥', url='https://t.me/leosupportx')
        ],[
        InlineKeyboardButton('Help 🆘', callback_data='help')
        ],[
        InlineKeyboardButton('➕ Add me to your group ➕', url='t.me/leosongdownloaderbot?startgroup=true')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('About ❗️', callback_data='about'),
        InlineKeyboardButton('User Info ❗', callback_data='info')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('Help 🆘', callback_data='help'),
        InlineKeyboardButton('About Dev 🧑‍💻', callback_data='aboutdev')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='close')
        ]]
    )
    INFO_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('About ❗️', callback_data='about'),
        InlineKeyboardButton('Help 🆘', callback_data='help')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='close')
        ]]
    )
    ABOUT_DEV_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('Help 🆘', callback_data='help'),
        InlineKeyboardButton('About ❗️', callback_data='about')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='close')
        ]]
    ) 
