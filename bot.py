from pyrogram import Client
from config import *

app = Client(
    "UltraFalBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

import modules.start
import modules.coffee
import modules.palm
import modules.tarot
import modules.numerology
import modules.astrology
import modules.dreams
import modules.aura
import modules.love
import modules.daily

import owner.admin
import owner.broadcast

app.run()
