from typing import Union
from fastapi import FastAPI
from mangum import Mangum
import uvicorn
import json

app = FastAPI()

@app.get("/hello")
async def root():
    return {"message`": "Hello World!"}

@app.get("/secondgreet")
async def second_root():
    return {"message`": "Hello Developer!"}

handler = Mangum(app)

