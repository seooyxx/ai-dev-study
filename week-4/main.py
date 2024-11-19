from enum import Enum
from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Hello World"}

@app.get("/home")
def home():
    return {"message" : "home"}

@app.get("/home/{name}")
def read_name(name: str):
    return {"name" : name}

@app.post("/")
def home_posst(msg: str):
    return {"Hello" : "POST", "msg" : msg}