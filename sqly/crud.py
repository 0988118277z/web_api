from sqlalchemy.orm import Session
from . import models, schemas

async def check_email(db: Session, umail):
    return db.query(models.Users).filter_by(umail = umail).first() 
    
async def check_user(db: Session, uid):
    return db.query(models.Users).filter_by(uid = uid).first() 

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
        
async def add_dns(db: Session, dns: schemas.DnsServerItem):
    db_dns = models.DnsServer(
        sname = dns.sname,
        sip = dns.sip,
        uid = dns.uid,
        uno = len(db.query(models.DnsServer).filter_by(uid = dns.uid).all()) + 1,
        status = True
        )
    db.add(db_dns)
    db.commit()
    db.refresh(db_dns)
    return db_dns
    
async def show_dns(db: Session, user_id):
    user_dns_list = db.query(models.DnsServer.uid, models.DnsServer.uno, models.DnsServer.sname, models.DnsServer.sip).filter_by(uid = user_id, status = True).all()
    return [ models.DnsServer(uid=item[0], uno=item[1], sname=item[2], sip=item[3]) for item in user_dns_list ]
    
async def change_dns(db: Session, dns: schemas.DnsServerChange):
    dns_user = db.query(models.DnsServer).filter_by(uid = dns.uid, uno = dns.uno).first()
    if dns_user and dns_user.status == 1:
        if dns.sname is not None:
            dns_user.sname = dns.sname
        if dns.sip is not None:
            dns_user.sip = dns.sip
            
        db.commit()
        db.refresh(dns_user)
        return dns_user
    else:
        return None

async def delete_dns(db: Session, dns: schemas.DnsServerChange):
    dns_user = db.query(models.DnsServer).filter_by(uid = dns.uid, uno = dns.uno).first()
    if dns_user:
        dns_user.status = 0
            
        db.commit()
        db.refresh(dns_user)
        return dns_user
    else:
        return None