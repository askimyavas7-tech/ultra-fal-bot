from pyrogram import filters
from bot import app
from config import OWNER_ID

@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(client, message):

    await message.reply_text(
"""
📊 Bot İstatistikleri

Kullanıcı sayısı: yakında eklenecek
"""
    )
