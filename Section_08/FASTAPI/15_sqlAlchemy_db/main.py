from sqlalchemy import create_engine, Column, Integer,String
from sqlalchemy.orm import sessionmaker , declarative_base , Session
from fastapi import FastAPI,Depends

app=FastAPI()

# database url
DATABASE_URL="sqlite:///./test.db"

# engine create (DB connection)
engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

# Session (DB operation le liye)
sessionLocal=sessionmaker(bind=engine)

# Base (model ke liye)
Base = declarative_base()

# Table (Model)
class todo(Base):
    __tablename__="todos"
    
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    Completed=Column(String)
    
# Table create  
Base.metadata.create_all(bind=engine)

# Dependency (DB session provide krega)
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@app.get("/")
def home(db:Session=Depends(get_db)):
    return{
        "message":"DB connected fine"
    }