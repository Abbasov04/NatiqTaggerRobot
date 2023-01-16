
import logging
from tglogging import TelegramLogHandler

# TGLOGGING Uygulamanızın logunu Telegram'a anlık göndermenizi sağlar. 

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        TelegramLogHandler(
            token="5636190781:AAGDOmFJmYDaJcPuW1lWyEAMgN-SwyycvRA", 
            log_chat_id=-1001805104889, 
            update_interval=2, 
            minimum_lines=1, # Her Mesajda gönderilecek satır sayısı
            pending_logs=200000),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("pyrogram - telethon")

logger.info("Telegram'a canlı log başlatıldı.")