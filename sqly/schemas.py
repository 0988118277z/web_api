from pydantic import BaseModel, validator, Field, root_validator
from datetime import date, datetime
from typing import Optional
from ipaddress import IPv4Address
from enum import Enum


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

class ParserType(Enum):
    A = 'A'
    AAAA = 'AAAA'
    ANY = 'ANY'
    CAA = 'CAA'
    CNAME = 'CNAME'
    MX = 'MX'
    NAPTR = 'NAPTR'
    NS = 'NS'
    PTR = 'PTR'
    SOA = 'SOA'
    SRV = 'SRV'
    TXT = 'TXT'
   
class DnsParser(BaseModel):
    uid: int = Field(..., example="user_id")
    uno: int | None = Field(None, example="user_server_number")
    domain: str = Field(..., example="domain")
    types: ParserType
    
    @validator('types')
    def parser_type_value(cls, v):
        return v.value
        
    