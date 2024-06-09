from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime, Date
from sqlalchemy.sql import func
from .database import Base


class Users(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    umail = Column(String(length=100), unique=True)
    uname = Column(String(length=50))
    upasswd = Column(String(length=255))
    ubirthday = Column(Date, nullable=True)
    uphone = Column(String(10), unique=True, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    is_active = Column(Boolean, default=True)

class UserSalts(Base):
    __tablename__ = "salts"
    
    slat_id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey('users.uid'))
    salt = Column(String(length=30))
    created_at = Column(DateTime, default=func.now())
    
class DnsServer(Base):
    __tablename__ = "dnsserver"
    
    sid = Column(Integer, primary_key=True, autoincrement=True)
    sname = Column(String(length=20))
    sip = Column(String(length=15))
    uid = Column(Integer, ForeignKey('users.uid'))
    uno = Column(Integer)
    updated_at = Column(DateTime, onupdate=func.now())
    
