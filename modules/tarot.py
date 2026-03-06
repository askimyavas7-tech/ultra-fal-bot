import random
from pyrogram import filters
from bot import app

cards = [
"The Sun ☀️ — Mutluluk",
"The Moon 🌙 — Gizem",
"The Star ⭐ — Umut",
"The Lovers ❤️ — Aşk",
"The Tower ⚡ — Değişim"
]

@app.on_message(filters.command("tarot"))
async def tarot(client, message):
    card = random.choice(cards)

    text = f"""
🃏 Tarot Kartın

{card}

Yorum:
Hayatında önemli bir enerji değişimi olabilir.
"""

    await message.reply_text(text)
