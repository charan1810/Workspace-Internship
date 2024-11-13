from typing import List
from fastapi import APIRouter,Depends,HTTPException
from database import SessionLocal,engine,Base
from sqlalchemy.orm import Session
from pydantic import BaseModel
import model
from authentication.auth import oauth2_scheme

router=APIRouter(
    tags=['employee data handling']
)
Base.metadata.create_all(bind=engine)
class createEmployeeRequest(BaseModel):
    username:str
    name:str
    password:str
    position:str
    salary:int
    level:int

class EmployeeBasicInfo(BaseModel):
    name: str
    position: str
    level: float

def get_db():
    db=SessionLocal()
    try:
        yield(db)
    finally:
        db.close()
@router.get("/employees/all_details", response_model=List[EmployeeBasicInfo])  # Use response_model to specify expected return type
def get_all_employee_details(db: Session = Depends(get_db)):
    # Use with_entities to select specific columns
    emp = db.query(
        model.Employee.name,
        model.Employee.position,
        model.Employee.level
    ).all()  # Add .all() to execute the query and return a list of results
    
    # Return the results as a list of dictionaries
    return [
        {
            "name": e.name, 
            "position": e.position, 
            "level": e.level} 
        for e in emp
        ]

@router.get("/employees/see_detail/{id}")
def get_employee_detail(id:int,token:str=Depends(oauth2_scheme),db: Session=Depends(get_db)):
    user=db.query(model.Employee).filter(model.Employee.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail='employee does not exist create an user')
    return user

@router.post("/employees/create_employee/")
def create_employee(level: float,employee:createEmployeeRequest,db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    required_level=6.52
    if level!=required_level:
        raise HTTPException(status_code=403, detail="Insufficient permissions to create an employee.")
    
    existing_employee=db.query(model.Employee).filter(model.Employee.username==employee.username).first()
    if existing_employee:
        raise HTTPException(status_code=400,detail='User already exists')
    new_employee=model.Employee(
        username=employee.username,
        name=employee.name,
        password=employee.password,
        position=employee.position,
        salary=employee.salary,
        level=employee.level
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    
    return new_employee

