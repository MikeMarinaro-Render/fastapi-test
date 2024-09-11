from typing import Optional
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test1")
async def root():
    x = requests.get('https://w3schools.com')
    print(x.status_code)

@app.get("/test2")
async def root():
    return {"message": "Test 2 success!"}
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
