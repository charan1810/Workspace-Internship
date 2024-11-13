from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

dataset = pd.read_csv(r"C:\Users\CHARAN\Datascience-programs\MachineLeaarningPrograms\NONLINEAR\Salary-Prediction\emp_sal.csv")
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,-1].values


regressor = KNeighborsRegressor(n_neighbors=5,weights='distance',p=2)
regressor.fit(X,y)

class PredictionRequest(BaseModel):
    years_of_experience:float

# fastapi 
app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")    

templates=Jinja2Templates(directory="templates")

@app.get("/")
async def get_form(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/predict/")
async def predict_salary(request:Request):
    form_data=await request.form()
    years_of_experience=float(form_data['years_of_experience'])
    prediction=regressor.predict([[years_of_experience]])
    return templates.TemplateResponse("index.html",{"request":request,"predicted_salary":round(prediction[0],2),"years_of_experience":years_of_experience})
