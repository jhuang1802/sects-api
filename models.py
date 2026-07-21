from pydantic import BaseModel, Field
import datetime as dt

class Show(BaseModel):
    date: dt.date
    city: str
    venue: str