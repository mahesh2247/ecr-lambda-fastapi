from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum
import uvicorn
import json

app = FastAPI()

@app.get("/hello", status_code=201)
async def root():
    return {"message`": "Hello REST API Demo using FastAPI deployed on Lambda!"}

@app.get("/{name}", status_code=201)
async def intro(name: str):
    return JSONResponse({"message`": f"Hello {name}! Nice to meet you"})

handler = Mangum(app)

