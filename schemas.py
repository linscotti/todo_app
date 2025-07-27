from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str = None


class TodoUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool

    class Config:
        orm_mode = True
