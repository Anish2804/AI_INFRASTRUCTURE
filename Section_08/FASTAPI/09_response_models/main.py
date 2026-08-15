from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str
    
class UserResponse(BaseModel):
    name:str
    age:int
    
    
@app.get("/user",response_model=UserResponse)
def get_user():
    return{
        "name":"anish",
        "age":23,
        "password":"987654"
    }
