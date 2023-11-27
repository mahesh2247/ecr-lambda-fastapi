from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum
from pydantic import BaseModel
import uvicorn
import json
import boto3
import os

class User(BaseModel):
    u_id: str
    name: str
    description: str

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["USERS_TABLE_NAME"])

app = FastAPI()

@app.get("/hello", status_code=201)
async def root():
    return {"message`": "Hello REST API Demo using FastAPI deployed on Lambda!"}

@app.get("/{name}", status_code=201)
async def intro(name: str):
    return JSONResponse({"message`": f"Hello {name}! Nice to meet you"})

@app.get("/users/{u_id}")
async def get_user(u_id: str):
    response = table.get_item(
        Key={
            'u_id': u_id
        }
    )
    item = response['Item']
    return item

@app.put("/users")
async def create_user(user: User):
    table.put_item(
        Item={
            'u_id': user.dict()['u_id'],
            'name': user.dict()['name'],
            'description': user.dict()['description']
        }
    )
    return {"u_id": user.dict()['u_id'], **user.dict()}

handler = Mangum(app)

