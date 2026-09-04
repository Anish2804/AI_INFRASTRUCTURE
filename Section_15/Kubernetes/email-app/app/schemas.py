from pydantic import BaseModel


class EmailCreate(BaseModel):
    email: str


class EmailResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True