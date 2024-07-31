from sqlalchemy import Column, String, Integer, BIGINT, Enum
from sqlalchemy.orm import relationship, declarative_base
from schemas.farm import FarmTypeEnum

Base = declarative_base()

class Farm(Base):
    __tablename__ = 'farm'
    id = Column(BIGINT, primary_key=True, index=True)
    gateway_id = Column(BIGINT)
    member_id = Column(BIGINT)
    address = Column(String(255))
    farm_type = Column(Enum(FarmTypeEnum))
    name = Column(String(255))
