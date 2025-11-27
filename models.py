from pydantic import BaseModel

class employee(BaseModel):
    name: str
    id: int
    age: int
    position: str
    department: str