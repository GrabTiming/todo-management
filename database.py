from sqlmodel import SQLModel, create_engine

# MySQL 连接
# mysql+pymysql://用户名:密码@主机:端口/数据库名
DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/todo_list"

engine = create_engine(
    DATABASE_URL,
    echo=True,  # 开发时显示SQL
    pool_size=5,  # 连接池大小
    max_overflow=10,  # 最大溢出连接数
    pool_timeout=30,  # 连接超时（秒）
    pool_recycle=1800,  # 连接回收时间（秒）
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

from sqlmodel import SQLModel, create_engine, Session

def get_session():
    with Session(engine) as session:
        yield session