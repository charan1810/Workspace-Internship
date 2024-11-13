from fastapi import FastAPI, Query , Path,HTTPException,Body,Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from database import cars
from starlette import status

app = FastAPI()

templates=Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")

class Car(BaseModel):
    make: Optional[str]
    model: Optional[str]
    year: Optional[int] = Field(..., ge=1970, lt=2024)
    price: Optional[float]
    engine: Optional[str] = "V4"
    autonomous: Optional[bool]
    sold: Optional[List[str]]

@app.get("/")
def root(request:Request):
    return templates.TemplateResponse("home.html",{'request':request,'title':"FastAPI - Home","Car":cars})
@app.get("/all_cars")
def get_all_cars():
    return cars

@app.get("/cars", response_class=HTMLResponse)
def get_cars(request: Request,number: Optional[int] = Query(10, ge=1, le=100)):
    response = []
    for car_id, car in list(cars.items())[:number]:
        response.append({str(car_id): car})  # Cast car_id to str for consistency with response model
    return templates.TemplateResponse("index.html",{'request':request,'cars':response,'title':'home'})

@app.get("/cars/{id}",response_model=Car)
def get_car_by_id(id:int=Path(...,ge=0,lt=1000)):
    car = cars.get(id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="couldn't find a car with the id")
    return car

@app.post("/cars",status_code=status.HTTP_201_CREATED)
def add_cars(body_cars:List[Car],min_id:Optional[int]=Body(0)):
    if len(body_cars)<1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No cars")
    min_id=len(cars.values())+min_id
    for car in  body_cars:
        while cars.get(min_id):
            min_id+=1
        cars[min_id]=car
        min_id+=1
        
@app.put("/cars/{id}",response_model=Dict[str,Car])
def update_car(id:int,car:Car=Body(...)):
    stored=cars.get(id)
    if not stored:
        raise HTTPException(status_code=status.HTTP_404NOT_FOUND,detail="No car with that od")
    stored = Car(**stored)
    new = car.dict(exclude_unset=True)
    new = stored.copy(update=new)
    cars[id]= jsonable_encoder(new)
    response={}
    response[id] = cars[id]
    return response

@app.delete("/cars/{id}")
def delete_car(id:int):
    if not cars.get(id):
        raise HTTPException(status_code=status.HTTP_404NOT_FOUND,detail="No car with that od")
    del cars[id]