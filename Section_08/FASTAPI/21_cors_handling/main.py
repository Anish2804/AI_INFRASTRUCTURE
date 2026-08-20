from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

#allowed origins(front-end url)

origins=[
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allowed Frontend
    allow_credentials=True, 
    allow_methods=["*"],      # GET,POST,PUT,DELETE
    allow_headers=["*"]
)

@app.get("/")
def home():
    return{
        "message":"CORS enable API"
    }