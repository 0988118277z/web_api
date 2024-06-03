from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix="/api/v1/hello",
    tags=["Hello"],
)

@router.get("/")
async def read_root():
    return "Hello World"


@router.get("/{item_id}")
async def read_item(item_id: int):
    return f"Hello {item_id}"