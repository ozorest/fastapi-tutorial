from enum import Enum
from typing import Optional

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet  = "resnet"
    lenet   = "lenet"


app = FastAPI()

fake_items_db = [{"item_name": "Ferrari"}, 
                 {"item_name": "BMW"}, 
                 {"item_name": "Audi"},
                 {"item_name": "Rolls Royce"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Path Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Query Parameters
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# Predefined values
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return { "model_name": model_name,
                 "message": "Deep Learning FTW!" }
    
    if model_name == ModelName.lenet:
        return { "model_name": model_name,
                 "message": "LeCNN all the images" }

    return { "model_name": model_name,
             "message": "Have some residuals" }

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# Optional parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Required query parameters
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item