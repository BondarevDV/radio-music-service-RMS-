from pydantic import BaseModel
from  datetime import date

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: str = None

