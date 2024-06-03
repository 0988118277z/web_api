from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix="/api/v1/account",
    tags=["Account"],
)

class AccountItem(BaseModel):
    uname: str
    upasswd: str
    udescription: Optional[str] = None
    uage: int
    uphone: Optional[int] = None
    
@router.post("/")
async def add_account(item: AccountItem):
    return item