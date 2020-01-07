from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = {
    0: {'name': "item 1", 'description': "description 1", 'price': 123},
    1: {'name': "item 2", 'description': "description 2", 'price': 234}
}


class Item(BaseModel):
    name: str
    description: str = None
    price: float


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/items/")
def read_items():
    return items


@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post('/items/')
def create_item(item: Item):
    number_of_items = len(items)
    items[number_of_items] = item
    return item
