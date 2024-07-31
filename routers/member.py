from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import member as member_service
from schemas.member import *
from models.member import *
from database import get_db
from schemas.member import Member as MemberSchema, MemberCreate
from services.member import register_member
from fastapi.responses import JSONResponse
import logging
import bcrypt

router = APIRouter()

@router.post("/register", response_model=MemberSchema)
def register_member(request: RegisterRequest, db: Session = Depends(get_db)):
    return member_service.register_member(db, request)

@router.post("/login", response_model=LoginResponse)
def login_member(request: LoginRequest, db: Session = Depends(get_db)):
    member = member_service.login_member(db, request)
    if member:
        # Generate token (assuming you have a method to generate JWT)
        token = "generated-jwt-token"
        return LoginResponse(token=token)
    raise HTTPException(status_code=401, detail="Invalid login credentials")

@router.get("/find", response_model=MemberSchema)
def find_member_by_login_id(login_id: str, db: Session = Depends(get_db)):
    return member_service.get_member_by_login_id(db, login_id)

@router.get("/findByEmail", response_model=MemberSchema)
def find_member_by_email(email: str, db: Session = Depends(get_db)):
    return member_service.get_member_by_email(db, email)


# logger = logging.getLogger(__name__)
#
# def verify_password(plain_password, hashed_password):
#     return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
#
# @router.post("/login")
# async def login(request: LoginRequest, db: Session = Depends(get_db)):
#     logger.info(f"Login request data: {request.dict()}")
#
#     user = db.query(Member).filter_by(login_id=request.loginId).first()
#     if not user or not verify_password(request.password, user.password):
#         logger.warning("Invalid credentials")
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#
#     logger.info(f"User {user.name} logged in successfully")
#     return JSONResponse(content={"name": user.name}, headers={
#         "Authorization": "accessToken",
#         "Set-Cookie": "refreshToken=refreshToken; Max-Age=1209600; Expires=Sun, 02 Jun 2024 08:33:53 GMT; HttpOnly"
#     })
#
# @router.post("/register")
# async def register(request: RegisterRequest, db: Session = Depends(get_db)):
#     db_user = Member(
#         login_id=request.loginId,
#         password=request.password,
#         name=request.name,
#         email=request.email
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return {"message": "Registration successful"}
#
# @router.get("/find/id")
# async def find_id(name: str, email: str, db: Session = Depends(get_db)):
#     user = db.query(Member).filter_by(name=name, email=email).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return FindIdResponse(loginId=user.login_id)