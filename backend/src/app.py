from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import file_router

app = FastAPI()


origins = [
    "http://localhost:5173",  # react
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(file_router)