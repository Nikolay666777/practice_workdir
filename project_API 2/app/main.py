from fastapi import FastAPI

app  = FastAPI()

@app.get("/")
def rear_root():
    return {"message": "Hello, FastApi"}

@app.get("/items/{item_id}")
def read_item(item_id:int):
    return {"item_id":item_id,"description":f" Item {item_id} description"}