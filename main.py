from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <-- import this
from dotenv import load_dotenv

load_dotenv()  # Load .env variables once

from app.routers import brainstorm

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your frontend URL when deploying, e.g. ["https://yourfrontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(brainstorm.router, prefix="/api/brainstorm", tags=["Brainstorm"])
