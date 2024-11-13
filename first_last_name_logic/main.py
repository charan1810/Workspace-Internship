from typing import Optional
from fastapi import FastAPI,Body
from pydantic import BaseModel,Field

class UserData(BaseModel):
    first_name:str
    last_name:str
    company_name:str
    password:Optional[str]

app = FastAPI()

@app.post("/get_username/")
def get_username_from_firstname_lastname_email(UserData:UserData):
    password="p99@2019"
    return {"username":UserData.first_name[0]+"."+UserData.last_name[-1]+"@"+UserData.company_name,"password":password}