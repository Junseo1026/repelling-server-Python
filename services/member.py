from sqlalchemy.orm import Session
from crud import member as member_crud
from schemas.member import RegisterRequest, LoginRequest
from models.member import Member

def register_member(db: Session, request: RegisterRequest):
    new_member = Member(
        email=request.email,
        login_id=request.login_id,
        name=request.name,
        password=request.password
    )
    return member_crud.create_member(db, new_member)

def login_member(db: Session, request: LoginRequest):
    member = member_crud.get_member_by_login_id(db, request.login_id)
    if member and member.password == request.password:
        return member
    return None

def get_member_by_login_id(db: Session, login_id: str):
    return member_crud.get_member_by_login_id(db, login_id)

def get_member_by_email(db: Session, email: str):
    return member_crud.get_member_by_email(db, email)
