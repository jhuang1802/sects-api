from fastapi import FastAPI
import storage
import database
from models import Show
from fastapi.middleware.cors import CORSMiddleware

database.init_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "Hello, World!"

@app.get("/shows")
def get_shows():
    return storage.get_all_shows()

@app.post("/shows")
def add_show(show: Show):
    return storage.add_show(show)