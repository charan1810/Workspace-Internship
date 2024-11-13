from fastapi import FastApi
from authentication import auth,authentication
from router import employeedetails

app=FastApi()
app.include_router(auth.router())
app.include_router(employeedetails.router())