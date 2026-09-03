import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = 5510300316

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

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # пересылаем админу текст, фото и любые другие сообщения от клиентов
    await context.bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(~filters.COMMAND, forward_to_admin))
app.run_polling()
