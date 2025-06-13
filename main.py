from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()  # Load .env variables once

from app.routers import brainstorm

app = FastAPI()

app.include_router(brainstorm.router, prefix="/api/brainstorm", tags=["Brainstorm"])
