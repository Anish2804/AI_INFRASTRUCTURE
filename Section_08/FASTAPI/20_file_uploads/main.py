from fastapi import FastAPI,HTTPException,UploadFile,File
from fastapi.staticfiles import StaticFiles
import os
import shutil

app=FastAPI()

# step-1 ensure upload folder exist
UPLOAD_DIR="uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
    
    
# step-2: static file setup
app.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")

#step-3: upload file api
@app.post("/upload")
def upload_file(file:UploadFile=File(...)):
    filename=file.filename
    file_path=os.path.join(UPLOAD_DIR,filename)
    
    if not filename:
        raise HTTPException(
            status_code=400,
            detail="File not Selected"
        )
        
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
        
        return{
            "message":"Files Uploaded Successfully",
            "fileName":filename,
            "file_URL":f"http://127.0.0.1:8000/files/{filename}"
        }
        
        
# step-4: Get file url api
@app.get("/files/{filename}")
def get_file(filename:str):
    file_path=os.path.join(UPLOAD_DIR,filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="Files not found"
        )
        
    return{
        "file_URL":f"http://127.0.0.1:8000/files/{filename}"
    }
    
    
@app.get("/")
def home():
    return{
        "message":"File uploaded api running"
    }