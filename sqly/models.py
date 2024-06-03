from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from database import Base

class UserInfo(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    umail = Column(String(length=100), unique=True)
    uname = Column(String(length=50))
    upasswd = Column(String(length=255))
    gender = Column(String(length=1))  
    ubirthday = Column(Date, nullable=True)
    uphone = Column(String(10), unique=True, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    is_active = Column(Boolean, default=True)

class Salts(Base):
    __tablename__ = "salts"
    
    slat_id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey('users.uid'))
    salt = Column(String(length=30))
    created_at = Column(DateTime, default=func.now())
    
