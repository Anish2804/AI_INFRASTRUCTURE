from fastapi import FastAPI , Depends , Header ,HTTPException

app= FastAPI()

def varify_token(token:str= Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code= 401,
            detail="Unauthorized"
        )
        
    return{
        "user":"Authorized user"
    }
    
@app.get("/secure_data")
def secure_data(user = Depends(varify_token)):
    return {
        "message":"secure data accessed",
        "user":user
    }

# def common_logic():
#     return {
#         "message":"common logic executed"
#     }
    
# @app.get("/home")
# def home(data= Depends(common_logic)):
#     return data

def current_user():
    return{
        "user":"guest"
    }
    
@app.get("/profile")
def profile(user=Depends(current_user)):
    return user

@app.get("/dashboard")
def dashboard(user=Depends(current_user)):
    return user