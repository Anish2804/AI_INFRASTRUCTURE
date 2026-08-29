from fastapi import FastAPI  # type: ignore[import-not-found]

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from Docker!"}


@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/test")
def health():
    return {"status": "testing!!!!!!!!!!"}