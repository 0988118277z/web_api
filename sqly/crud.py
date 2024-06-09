from sqlalchemy.orm import Session
from . import models, schemas

async def check_email(db: Session, umail):
    return db.query(models.Users).filter_by(umail = umail).first() 

async def add_user(db: Session, user: schemas.UserItem):
    db_user = models.Users(
        uname = user.uname,
        upasswd = user.upasswd,
        umail = user.umail,
        ubirthday = user.ubirthday,
        uphone = user.uphone
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def passwd_reset(db: Session, user: schemas.PaaawdChange):
    pc_user = db.query(models.Users).filter_by(umail = user.umail).first()
    if pc_user:
        pc_user.upasswd = user.upasswd
        
        db.commit()
        db.refresh(pc_user)

        return pc_user
    else:
        return None