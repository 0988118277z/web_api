from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqly.database import get_db
from sqly import schemas, crud

router = APIRouter(
    prefix="/api/v1/app",
    tags=["App"],
)

@router.get("/")
async def select():
    return 
    
@router.post("/")
async def add():
    return 
    
@router.put("/")
async def update():
    return 

@router.delete("/")
async def delete():
    return   
