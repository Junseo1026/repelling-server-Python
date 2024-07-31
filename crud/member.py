from sqlalchemy.orm import Session
from models.member import Member

def get_member_by_login_id(db: Session, login_id: str):
    return db.query(Member).filter(Member.login_id == login_id).first()

def get_member_by_email(db: Session, email: str):
    return db.query(Member).filter(Member.email == email).first()

def create_member(db: Session, member: Member):
    db.add(member)
    db.commit()
    db.refresh(member)
    return member
