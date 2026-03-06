from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import app

TEXT = """
🔮 ULTRA FAL BOTU

Bakabileceğim fallar:

☕ Kahve Falı
✋ El Falı
🃏 Tarot
🔢 Numeroloji
🌙 Rüya Yorumu
🪐 Astroloji
🌈 Aura
❤️ Aşk Uyumu

Bir komut yaz veya fotoğraf gönder.
"""

keyboard = InlineKeyboardMarkup([
[InlineKeyboardButton("☕ Kahve Falı", callback_data="coffee")],
[InlineKeyboardButton("✋ El Falı", callback_data="palm")],
[InlineKeyboardButton("🃏 Tarot", callback_data="tarot")],
[InlineKeyboardButton("❤️ Aşk Uyumu", callback_data="love")]
])

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(TEXT, reply_markup=keyboard)
