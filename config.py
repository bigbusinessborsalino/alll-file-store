# Don't Remove Credit
# TitanXBots
# Dev - Yash



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#File Auto Delete
FILE_AUTO_DELETE = int(os.environ.get("FILE_AUTO_DELETE", "3600")) # auto delete in seconds


#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://AllMight:23032020@cluster0.8uhy3pu.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Clustero") # Don't Change Database Name

#force sub channel id, if you want to enable force sub (Use different ForceSub Channel ID)
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002407082876"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002453718383"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002675518101"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1001472253105"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/976a689593cb01a4f8376-e87554005ac58b6c24.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/976a689593cb01a4f8376-e87554005ac58b6c24.jpg") 

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ꜰɪʟᴇꜱᴛᴏʀᴇ ʙᴏᴛ ᴛᴏ ꜱᴛᴏʀᴇ ᴀɴᴅ ꜱʜᴀʀᴇ - ꜰɪʟᴇꜱ, ᴅᴏᴄᴜᴍᴇɴᴛꜱ, ᴇᴛᴄ..... \n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ 𝟦 ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!</b>"
ABOUT_TXT = "<b>✯ Creator : <a href='https://t.me/STRONGEST_MARINE'>This Person</a>\n✯ Language : <code>Python3</code>\n✯ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio</a>\n✯ Source Code : <a href='https://github.com/TitanXBots/FileStore-Bot'> </b>"
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "👋Hey Friend, 🚫Don't send any messages to me directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(7911798212)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
