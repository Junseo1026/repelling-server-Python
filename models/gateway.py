from sqlalchemy import Column, String, BIGINT, Boolean
from database import Base

class Gateway(Base):
    __tablename__ = 'gateway'
    id = Column(BIGINT, primary_key=True, index=True)
    is_activated = Column(Boolean, default=False)
    ipv4 = Column(String(255))
    serial_id = Column(String(255))
