from AylinRobot.config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AylinRobot import LOGGER    
class Button(object):
  
### START BUTTONU    
      START_BUTTONS = InlineKeyboardMarkup(
        [[
      InlineKeyboardButton("👾 Botlist", url=f"https://t.me/{Config.BOTLIST}"),
      InlineKeyboardButton("📢 Kanal", url=f"https://t.me/{Config.SUPPORT}"),
        ],[                  
      InlineKeyboardButton('💠 Kömək', callback_data='help'),
        ],[        
      InlineKeyboardButton('➕ Məni Qrupa Əlavə Et ➕', url=f"https://t.me/{Config.BOT_USERNAME}?startgroup=true"),
        ],[                
      InlineKeyboardButton('Sahibim🧑‍💻',  url=f"https://t.me/{Config.OWNER_NAME}"),
      InlineKeyboardButton("🎵 Playlist", url=f"https://t.me/{Config.PLAYLIST_NAME}"),
        ]]
    )
      HELP_BUTTONS = InlineKeyboardMarkup(
        [[
      InlineKeyboardButton('🎵 Musiqi', callback_data='musıc'),
      InlineKeyboardButton('⭐ Telegraph', callback_data='tg')
        ],[
      InlineKeyboardButton('🎮 Oyunlar', callback_data='oyun'),
      InlineKeyboardButton('🇦🇿 Şəhidlər', callback_data='sehıd'),
        ],[        
      InlineKeyboardButton('🌀 Əyləncə', callback_data='eylence'),
      InlineKeyboardButton('Əlavələr', callback_data='elave'),
        ],[
      InlineKeyboardButton('👨‍💻 Sahib Əmrləri', callback_data='sahib'), 
        ],[        
      InlineKeyboardButton('↪️ Geri Qayıt', callback_data='home'),
        ]]
    )
    
    
      MUSIC_BUTTONS = InlineKeyboardMarkup(
        [[
      InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )
      TELEGRAPH_BUTTONS = InlineKeyboardMarkup(
        [[
      InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )
      SEHID_BUTTONS = InlineKeyboardMarkup(
        [[
      InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )        
      OYUN_BUTTONS = InlineKeyboardMarkup(
        [[
      InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )
      EYLENCE_BUTTONS = InlineKeyboardMarkup(
        [[
      InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )     
      SAHIB_BUTTONS = InlineKeyboardMarkup(
        [[
      InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )
      ELAVE_BUTTONS = InlineKeyboardMarkup(
        [[
      InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    ) 