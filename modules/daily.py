import random
from pyrogram import filters
from bot import app

daily = [
"Bugün şanslı bir gün.",
"Yeni fırsatlar kapıda.",
"Beklenmedik bir mesaj alabilirsin.",
"Duygusal bir gelişme olabilir."
]

@app.on_message(filters.command("gunluk"))
async def daily_fortune(client, message):

    text = random.choice(daily)

    await message.reply_text(
f"""
🔮 Günlük Fal

{text}
"""
    )
