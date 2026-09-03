from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/api/message")
def message():
    return {"message": "Hello from FastAPI + Docker!"}

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")