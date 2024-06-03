from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix="/api/v1/img-convert",
    tags=["Image convert"],
)