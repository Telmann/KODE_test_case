from pydantic import BaseModel


class User(BaseModel):
    login: str
    password: str


class Note(BaseModel):
    content: str
    user_id: int


class TokenData(BaseModel):
    login: str | None = None
