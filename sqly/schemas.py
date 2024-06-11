from pydantic import BaseModel, validator, Field, root_validator
from datetime import date, datetime
from typing import Optional
from ipaddress import IPv4Address


class UserItem(BaseModel):
    umail: str = Field(..., example="user_email")
    uname: str = Field(..., example="user_name")
    upasswd: str = Field(..., example="user_password")
    ubirthday: Optional[date] = None
    uphone: str = Field(..., example="user_phone")

class PaaawdChange(BaseModel):
    umail: str = Field(..., example="user_email")
    upasswd: str = Field(..., example="user_new_password")

class UserId(BaseModel):
    uid: int = Field(..., example="user_id")

class DnsServerItem(BaseModel):
    sname: str = Field(..., example="dns_server_name")
    sip: str = Field(..., example="dns_server_ip")
    uid: int = Field(..., example="user_id")
    
    @validator('sip')
    def validate_ipv4_network(cls, v, values):
        try:
            return str(IPv4Address(v))
        except ValueError as e:
            raise ValueError(f"{v} does not appear to be an IPv4 network")
            
class DnsServerChange(BaseModel):
    sname: str = Field(None, example="dns_server_name")
    sip: str = Field(None, example="dns_server_ip")
    uid: int = Field(..., example="user_id")
    uno: int = Field(..., example="user_server_number")
    
    @validator('sip')
    def validate_ipv4_network(cls, v, values):
        try:
            return str(IPv4Address(v))
        except ValueError as e:
            raise ValueError(f"{v} does not appear to be an IPv4 network")
            
class DnsServerDelete(BaseModel):
    uid: int = Field(..., example="user_id")
    uno: int = Field(..., example="user_server_number")
    