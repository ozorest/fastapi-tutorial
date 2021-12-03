from typing import Optional, List

from fastapi import FastAPI, Query

app = FastAPI()


# Validations
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, 
                                              min_length=3, 
                                              max_length=50, 
                                              regex="^fixedquery$")):
    results = {"items": [
                        {"item_id": "Foo"}, 
                        {"item_id": "Bar"}
                        ]}
    if q:
        results.update({"q": q})
    return results

# Default values
@app.get("/items/")
async def read_items(q: Optional[str] = Query("fixedquery", min_length=3)):
    results = {"items": [
                        {"item_id": "Foo"}, 
                        {"item_id": "Bar"}
                        ]}
    if q:
        results.update({"q": q})
    return results

# Required values
@app.get("/items/")
async def read_items(q: Optional[str] = Query(..., min_length=3)):
    results = {"items": [
                        {"item_id": "Foo"}, 
                        {"item_id": "Bar"}
                        ]}
    if q:
        results.update({"q": q})
    return results

# # Multiple values - using typing
@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items

# Multiple values - using list
# FastAPI don't check contents in this case
@app.get("/items/")
async def read_items(q: list = Query([])):
    query_items = {"q": q}
    return query_items

# Declaring metadata
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None, 
        title="Query String", 
        description="Query string for the items to search in database",
        min_length=3)
    ):
    results = {"items": [
                        {"item_id": "Foo"}, 
                        {"item_id": "Bar"}
                        ]}
    if q:
        results.update({"q": q})
    return results

# Alias parameters
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [
                        {"item_id": "Foo"}, 
                        {"item_id": "Bar"}
                        ]}
    if q:
        results.update({"q": q})
    return results

# Deprecated values
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None, 
        alias="item-query",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        title="Query String", 
        description="Query string for the items to search in database",
        deprecated=True)
    ):
    results = {"items": [
                        {"item_id": "Foo"}, 
                        {"item_id": "Bar"}
                        ]}
    if q:
        results.update({"q": q})
    return results