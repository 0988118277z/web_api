from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqly.database import get_db
from sqly import schemas, crud

router = APIRouter(
    prefix="/api/v1/dns",
    tags=["DNS"],
)

@router.get("/dns_server")
async def show_dns_server(db: Session = Depends(get_db), query: schemas.UserId = Depends()):
    check_user = await crud.check_user(db=db, uid=query.uid)
    if check_user:
        dns_info = await crud.show_dns(db=db, user_id=query.uid)
        return dns_info
    raise HTTPException(status_code=400, detail="User does not exist")
    
@router.post("/dns_server")
async def add_dns_server(dns: schemas.DnsServerItem, db: Session = Depends(get_db)):
    check_user = await crud.check_user(db=db, uid=dns.uid)
    if check_user:
        await crud.add_dns(db=db, dns=dns)
        return {"detail": "DNS server create complete"}
    raise HTTPException(status_code=400, detail="User does not exist")
    
@router.put("/dns_server")
async def update_dns_server(dns: schemas.DnsServerChange, db: Session = Depends(get_db)):
    check_user = await crud.check_user(db=db, uid=dns.uid)
    if check_user:
        check_data = await crud.change_dns(db=db, dns=dns)
        if check_data:
            return {"detail": "DNS server update complete"}
        else:
            raise HTTPException(status_code=400, detail="UID or UNO does not exist")
    raise HTTPException(status_code=400, detail="User does not exist")

@router.delete("/dns_server")
async def delete_dns_server(dns: schemas.DnsServerDelete, db: Session = Depends(get_db)):
    check_user = await crud.check_user(db=db, uid=dns.uid)
    if check_user:
        check_data = await crud.delete_dns(db=db, dns=dns)
        if check_data:
            return {"detail": "DNS server delete complete"}
        else:
            raise HTTPException(status_code=400, detail="UID or UNO does not exist")
    raise HTTPException(status_code=400, detail="User does not exist")
