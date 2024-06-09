from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base

# username = os.getenv('api_username')
# password = os.getenv('api_password')
# ip = os.getenv('api_ip')
# port = os.getenv('api_port')
# databasename = os.getenv('api_dbname')
username = 'root'
password = 'Aa123456'
ip = '127.0.0.1'
port = '3306'
databasename = 'api'

# 連接到的URL
URL_DATABASE=f'mysql+mysqlconnector://{username}:{password}@{ip}:{port}/{databasename}'

# 用create_engine對這個URL_DATABASE建立一個引擎
engine = create_engine(URL_DATABASE)

# 使用sessionmaker來與資料庫建立一個對話，記得要bind=engine，這才會讓專案和資料庫連結
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()