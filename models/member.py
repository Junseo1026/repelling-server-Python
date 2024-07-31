from sqlalchemy import Column, String, Integer, BIGINT
from database import Base

class Member(Base):
    __tablename__ = 'member'
    id = Column(BIGINT, primary_key=True, index=True)
    email = Column(String(255))
    login_id = Column(String(255))
    name = Column(String(255))
    password = Column(String(255))
