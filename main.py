from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "F# World AHHHHHHH"}

@app.get("/return_one")
def return_one():
    return {"number": 1}