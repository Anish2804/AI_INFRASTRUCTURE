import time
import asyncio
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return{
        "message":"Async API"
    }

# synchronous 
# def task():
#     time.sleep(3)
#     return "Done"

# Asynchronous
# async def task():
#     await asyncio.sleep(3)
#     return "Done"