from fastapi import APIRouter, Request
from telegram import Update
from bot.handler import create_bot_app

router = APIRouter()
bot_app = create_bot_app()

@router.post("/webhook")
async def telegram_webhook(request: Request):
    json_data = await request.json()
    update = Update.de_json(json_data, bot_app.bot)
    await bot_app.process_update(update)
    return {"status": "ok"}
