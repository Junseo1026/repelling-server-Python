from sqlalchemy.orm import Session
from crud import refresh_token as refresh_token_crud
from models.jwt import RefreshToken

def save_refresh_token(db: Session, member_id: int, token: str):
    refresh_token_crud.delete_refresh_token_by_member_id(db, member_id)
    new_refresh_token = RefreshToken(member_id=member_id, refresh_token=token)
    return refresh_token_crud.create_refresh_token(db, new_refresh_token)

def get_refresh_token(db: Session, member_id: int):
    return refresh_token_crud.get_refresh_token_by_member_id(db, member_id)

def delete_refresh_token(db: Session, member_id: int):
    return refresh_token_crud.delete_refresh_token_by_member_id(db, member_id)
