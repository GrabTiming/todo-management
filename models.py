# coding = utf-8
#!/usr/bin/env python
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # 用户邮箱，用于登录和联系，必须唯一且建立索引
    email: str = Field(
        unique=True,
        index=True,
        sa_column_kwargs={"comment": "用户邮箱，用于登录和联系，必须唯一且建立索引"}
    )
    # 用户密码的哈希值，用于安全验证
    password: str = Field(
        sa_column_kwargs={"comment": "用户密码的哈希值，用于安全验证"}
    )
    # 用户账户创建时间，使用UTC时间戳
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"comment": "用户账户创建时间，使用UTC时间戳"}
    )

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # 任务标题，简要描述任务内容，建立索引便于搜索
    title: str = Field(
        index=True,
        sa_column_kwargs={"comment": "任务标题，简要描述任务内容，建立索引便于搜索"}
    )
    # 任务详细描述，可选字段
    description: Optional[str] = Field(
        default=None,
        sa_column_kwargs={"comment": "任务详细描述，可选字段"}
    )
    # 任务状态，可选值为"pending"(待办)、"in_progress"(进行中)、"completed"(已完成)，默认为"pending"
    status: str = Field(
        default="pending",
        sa_column_kwargs={"comment": "任务状态，可选值为\"pending\"(待办)、\"in_progress\"(进行中)、\"completed\"(已完成)，默认为\"pending\""}
    )
    # 任务截止日期，可选字段
    due_date: Optional[datetime] = Field(
        default=None,
        sa_column_kwargs={"comment": "任务截止日期，可选字段"}
    )
    # 任务创建时间，使用UTC时间戳
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"comment": "任务创建时间，使用UTC时间戳"}
    )
    # 任务所有者的用户ID，外键关联到User模型的id字段
    owner_id: int = Field(
        sa_column_kwargs={"comment": "任务所有者的用户ID，外键关联到User模型的id字段"}
    )

class Test(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)