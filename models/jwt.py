from sqlalchemy import Column, String, Integer, BIGINT
from database import Base

class RefreshToken(Base):
    __tablename__ = 'refresh_token'
    id = Column(BIGINT, primary_key=True, index=True)
    member_id = Column(BIGINT)
    refresh_token = Column(String(255))
