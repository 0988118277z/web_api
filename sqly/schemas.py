from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class UserItem(BaseModel):
    umail: str
    uname: str
    upasswd: str
    ubirthday: Optional[date] = None
    uphone: str

class PaaawdChange(BaseModel):
    umail: str
    upasswd: str
