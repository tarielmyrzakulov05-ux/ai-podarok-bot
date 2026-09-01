import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Это AI Podarok — персональные ИИ-подарки в Бишкеке.\n\n"
        "Что можно заказать:\n"
        "🎨 Аватар в мультяшном стиле — от 300 сом\n"
        "🎂 Портрет-открытка на день рождения — от 500 сом\n"
        "💍 Свадебное приглашение с ИИ-иллюстрацией — от 800 сом\n\n"
        "Чтобы заказать — просто пришли сюда:\n"
        "1. Какой формат хочешь\n"
        "2. Своё фото (если нужно)\n"
        "3. Пожелания (стиль, текст, цвета)\n\n"
        "Мы ответим и пришлём результат в течение нескольких часов!"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
