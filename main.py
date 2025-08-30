# coding=utf-8

from fastapi import FastAPI, Depends
from sqlmodel import Session

import database
import models
import uvicorn
from database import engine, get_session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    print("Creating database and tables...")
    database.create_db_and_tables()
@app.post("/users/")
def create_user(user: models.User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.get("/users/")
def read_users(session: Session = Depends(get_session)):
    users = session.query(models.User).all()
    return users

@app.get("/hello")
def hello():
    return {"message": "Hello World"}


# 添加程序入口点，可以指定端口
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)

