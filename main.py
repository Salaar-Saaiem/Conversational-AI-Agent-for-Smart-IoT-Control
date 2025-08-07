from fastapi import FastAPI
from api.webhook import router
from config.logger import logger

app = FastAPI()
app.include_router(router)

logger.info("🚀 FastAPI app running")
