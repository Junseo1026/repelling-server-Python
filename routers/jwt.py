from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import token as token_service
from utils import jwt as jwt_utils
from database import get_db

router = APIRouter()

@router.post("/generate", response_model=str)
def generate_token(username: str):
    return jwt_utils.generate_access_token(username)

@router.post("/refresh", response_model=str)
def refresh_token(username: str):
    return jwt_utils.generate_refresh_token(username)

@router.get("/validate", response_model=bool)
def validate_token(token: str):
    return jwt_utils.validate_token(token)
