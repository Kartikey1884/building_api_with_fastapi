# from pydantic import BaseModel, Field,StrictInt
# from typing import Optional

# class employee(BaseModel):
#     name: str=Field(..., min_length=3, max_length=50,pattern="^[A-Za-z ]+$")#for pydantic <2.0 use regex instead of pattern
#     id: int=Field(..., gt=0,title="Employee ID must be a positive integer")
#     #age:StrictInt|None=Field(..., gt=18, lt=70)
#     age: StrictInt|None=Field(..., gt=18, lt=70,nullable=True)
#     position: str
#     department: str=Field(..., min_length=2, max_length=50) 
from pydantic import BaseModel, Field, StrictInt

class employee(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, pattern="^[A-Za-z ]+$")
    id: int = Field(..., gt=0, title="Employee ID must be a positive integer")
    age: StrictInt | None = Field(default=None, gt=18, lt=70, nullable=True)
    position: str
    department: str = Field(..., min_length=2, max_length=50)
