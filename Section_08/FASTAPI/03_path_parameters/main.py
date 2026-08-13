from fastapi import FastAPI

app=FastAPI()

# home route
@app.get("/")
def home():
    return {"message":"Welcom to FASTAPI"}


# about route
@app.get("/about")
def about():
    return {"message":"This is about page"}

# user route
@app.get("/users/{user_id:int}")
def get_users(user_id):
    return {"user_id":user_id}