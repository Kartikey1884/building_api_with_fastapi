#create an app using fastapi with 5 endpoints to perform CRUD operations on employee data
# Each employee has the following attributes: name, id, age, position, department
# Use pydantic models to define the employee schema and store the employee data in a list.

from fastapi import FastAPI,HTTPException
#from models import employee
from models_val import employee
from typing import List

app = FastAPI()
employees_db:List[employee] = []

#1.read all employees
@app.get("/employees", response_model = List[employee])
def get_employees():
    return employees_db


#2.read specific employee
@app.get("/employees/{emp_id}", response_model=employee)
def get_employee(emp_id:int):
    for index,emp in enumerate(employees_db):
        if emp.id == emp_id:
            return employees_db[index]
    raise HTTPException(status_code=404, detail="Employee not found")


# 3.create employee/add an employee
@app.post("/add_employees", response_model=employee)
def add_employee(new_emp:employee):
    for emp in employees_db:
        if emp.id==new_emp.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
        
    employees_db.append(new_emp)
    return new_emp


#4.update employee
@app.put("/update_employee/{emp_id}", response_model=employee)
def update_employee(emp_id:int, updated_emp:employee):
    for index,emp in enumerate(employees_db):
        if emp.id == emp_id:
            employees_db[index] = updated_emp
            return employees_db[index]
    raise HTTPException(status_code=404, detail="Employee not found")


#5.delete employee
@app.delete("/delete_employee/{emp_id}")
def delete_employee(emp_id:int):
    for index,emp in enumerate(employees_db):
        if emp.id == emp_id:
            del employees_db[index]
            return {"message":"Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")