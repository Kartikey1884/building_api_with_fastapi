from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

app = FastAPI()

@app.get("/user", response_model=User)

def get_user():
    return User(id=1, name="kartikey", email="kartike112@gmail.com")