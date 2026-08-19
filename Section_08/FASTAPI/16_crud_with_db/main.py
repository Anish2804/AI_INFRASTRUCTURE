from sqlalchemy import create_engine, Column, Integer,String
from sqlalchemy.orm import sessionmaker , declarative_base , Session
from fastapi import FastAPI,Depends, HTTPException

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
class Todo(Base):
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
        
        
# create API
@app.post("/todos")
def create_todo(title:str,db:Session=Depends(get_db)):
    todo=Todo(title=title,Completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo created",
        "data":todo
    }
    
    
# read all data
@app.get("/todos")
def get_todos(db:Session=Depends(get_db)):
    todos = db.query(Todo).all()
    return{
        "Total":len(todos),
        "data":todos
    }
    
    
# read data based on id
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int, db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# update data
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    
    if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.title=title
    
    db.commit()
    db.refresh(todo)
    return{
        "message":"updated",
        "data":todo
    }
    
    
# delete api
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo= db.query(Todo).filter(Todo.id==todo_id).first()
    
    if not todo:
                raise HTTPException(status_code=404, detail="Todo not found")
            
    db.delete(todo)
    db.commit()
    
    return{
        "message":"TODO DELETED"
    }
    
    