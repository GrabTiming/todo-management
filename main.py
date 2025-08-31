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

@app.get("/hello")
def hello():
    return {"message": "Hello World"}

# =========================== 以下是练习用户登录校验 ===================
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


def encipher(password: str):
    """加密字符串 与数据库对比"""
    # todo 做加密处理
    return password


def login(username: str, password: str, session: Session = Depends(get_session)):

    user = session.query(models.User).filter(models.User.username == username).first()
    password = encipher(password)
    if user and user.password == password:
        return user

    return {"code": 401, "message": "用户名或密码错误"}

# ================================  以下是练习fast-api框架 ============================================

@app.post("/tests/create")
def create_test(test: models.Test, session: Session = Depends(get_session)):
    session.add(test)
    session.commit()
    session.refresh(test)
    return test

@app.get("/tests/")
def get_tests(score: float = 0, session: Session = Depends(get_session)):

    tests = session.query(models.Test).filter(models.Test.score >= score) .all()
    return tests

@app.get("/tests/")
def get_tests(score: float = 0, session: Session = Depends(get_session)):

    tests = session.query(models.Test).filter(models.Test.score >= score) .all()
    return tests


# 添加程序入口点，可以指定端口
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)

