from sqlalchemy.orm import Session
from models.jwt import RefreshToken

def get_refresh_token_by_member_id(db: Session, member_id: int):
    return db.query(RefreshToken).filter(RefreshToken.member_id == member_id).first()

def create_refresh_token(db: Session, refresh_token: RefreshToken):
    db.add(refresh_token)
    db.commit()
    db.refresh(refresh_token)
    return refresh_token

def delete_refresh_token_by_member_id(db: Session, member_id: int):
    db.query(RefreshToken).filter(RefreshToken.member_id == member_id).delete()
    db.commit()
