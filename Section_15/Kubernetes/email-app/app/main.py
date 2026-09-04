from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse, RedirectResponse
from sqlalchemy.orm import Session

from .database import engine, get_db
from . import models, schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/add-email")
def add_email(
    email: schemas.EmailCreate,
    db: Session = Depends(get_db)
):
    new_email = models.Email(email=email.email)

    db.add(new_email)
    db.commit()
    db.refresh(new_email)

    return RedirectResponse("/", status_code=303)


@app.get("/emails", response_model=list[schemas.EmailResponse])
def get_emails(db: Session = Depends(get_db)):
    return db.query(models.Email).all()