from AylinRobot.config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
  
### START BUTTONU 

START_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('📢 Kanal', url=f"https://t.me/{Config.CHANNEL}"),
InlineKeyboardButton("💬 Söhbət Qrupu", url=f"https://t.me/{Config.SUPPORT}"),
],[
InlineKeyboardButton('📚 Kömək', callback_data='help'),
],[        
InlineKeyboardButton('➕ Məni Qrupa Əlavə Et ➕', url=f"https://t.me/{Config.BOT_USERNAME}?startgroup=true"),
],[                
InlineKeyboardButton('👨‍💻 𝑺𝒂𝒉𝒊𝒃𝒊𝒎',  url=f"https://t.me/elemedeala"),
]]
#### KÖMƏK BUTTONU

HELP_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🎧 Musiqi', callback_data='musıc'),
InlineKeyboardButton('⭐ Telegraph', callback_data='tg')
],[
InlineKeyboardButton('🎮 Oyunlar', callback_data='oyun'),
InlineKeyboardButton('🇦🇿 Şəhidlər', callback_data='sehıd'),
],[        
InlineKeyboardButton('🌀 Əyləncə', callback_data='eylence'),
InlineKeyboardButton('♾️ Əlavələr', callback_data='elave'),
],[
InlineKeyboardButton('🔍 Axtarış', callback_data='axtar'),
InlineKeyboardButton('🛎 Tagger', callback_data='tag'),    
],[
InlineKeyboardButton('👨‍💻 Sahib Əmrləri', callback_data='sahib'),
],[    
InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='home'),]])

### GERİ BUTTONU    

MUSIC_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),]])
TELEGRAPH_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),]])
SEHID_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),]])        
OYUN_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),]])
EYLENCE_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),]])     
SAHIB_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),]])
ELAVE_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),]])
AXTAR_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),]])
TAGGER_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),]])
BH_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),   
InlineKeyboardButton('↪️ Geri Qayıt', callback_data='home'),]])
GS_BUTTONS = InlineKeyboardMarkup(
[[InlineKeyboardButton('🔐 Bağla', callback_data='close'),]])   