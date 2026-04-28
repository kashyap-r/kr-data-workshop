# Think of this as your API gateway layer
import logging
from fastapi import FastAPI
from app.routes import router

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

app.include_router(router)
