import random
from pyrogram import filters
from bot import app

numbers = [
"1 — Liderlik enerjisi",
"2 — Uyum ve denge",
"3 — Yaratıcılık",
"7 — Spiritüel güç",
"9 — Bilgelik"
]

@app.on_message(filters.command("numeroloji"))
async def numerology(client, message):

    result = random.choice(numbers)

    await message.reply_text(
f"""
🔢 Numeroloji Analizi

Enerjin:
{result}
"""
)
