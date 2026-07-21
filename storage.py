from fastapi import HTTPException
from models import Show
import database

def get_all_shows():
    shows = []
    rows = database.get_all_shows()
    for row in rows:
        shows.append(dict(row))
    return shows

def add_show(show: Show):
    row = database.add_show(show.date, show.city, show.venue)
    return dict(row)