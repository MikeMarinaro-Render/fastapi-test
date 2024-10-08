from typing import Optional
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/catapi")
async def root():
    x = requests.get('https://api.thecatapi.com/v1/images/search')
    return(x.content)

@app.get("/test")
async def root():
    x = requests.get('https://fastapi-test-psmh.onrender.com/catapi', timeout=40, allow_redirects=True)
    return {x.content}
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
