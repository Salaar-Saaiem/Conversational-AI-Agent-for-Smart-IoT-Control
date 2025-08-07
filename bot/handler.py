from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from config.settings import BOT_TOKEN
from config.logger import logger

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Received /start command")
    await update.message.reply_text("🤖 Hello! I'm your AI-IoT Assistant.")

def create_bot_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    return app
