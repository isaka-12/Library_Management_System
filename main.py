from typing import Union

from fastapi import FastAPI
from models.schemas import Item

app = FastAPI()



@app.get("/")
def read_root(item:Item):
    return {"item":item.name}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/add_item")
def add_item(item:Item):
    return{"item_name":item.name,"price":item.price}

@app.delete("/items/delete_item{item_id}")
def delete_item(item_id:int):
    return {"item_id":item_id}