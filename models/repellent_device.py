from sqlalchemy import Column, String, Integer, BIGINT, Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class RepellentDevice(Base):
    __tablename__ = 'repellent_device'
    id = Column(BIGINT, primary_key=True, index=True)
    is_activated = Column(Boolean, default=False)
    is_working = Column(Boolean, default=False)
    farm_id = Column(BIGINT, ForeignKey('farm.id'))
    latitude = Column(String(255))
    longitude = Column(String(255))
    name = Column(String(255))
    serial_id = Column(String(255))

    repellent_data = relationship("RepellentData", back_populates="repellent_device")