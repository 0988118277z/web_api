from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqly.database import get_db
from sqly import schemas, crud

router = APIRouter(
    prefix="/api/v1/user",
    tags=["User"],
)

@router.post("/")
async def add_user(user: schemas.UserItem, db: Session = Depends(get_db)):
    check_mail = await crud.check_email(db=db, umail=user.umail)
    if check_mail:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        await crud.add_user(db=db, user=user)
        return {"detail": "Account create complete"}
    
@router.put("/")
async def passwd_reset(user: schemas.PaaawdChange, db: Session = Depends(get_db)):
    check_mail = await crud.check_email(db=db, umail=user.umail)
    if check_mail:
        await crud.passwd_reset(db=db, user=user)
        return {"detail": "Password reset complete"}
    else:
        raise HTTPException(status_code=400, detail="Email does not exist")
        
    
