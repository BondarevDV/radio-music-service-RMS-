from  fastapi import FastAPI
from  schemas import Book


app = FastAPI()



@app.get('/')
def home():
    return {"key": "hello"}


@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    return {"key": pk, "q": q}



@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {"key": pk, "item": item}


@app.post('/book')
def create_book(item: Book):
    return item


