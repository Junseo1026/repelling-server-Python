from sqlalchemy import Column, String, Integer, BIGINT, Enum, ForeignKey
from database import Base
from schemas.repellent_data import DetectionTypeEnum
from sqlalchemy.orm import relationship
from models.repellent_sound import RepellentSound
from models.repellent_device import RepellentDevice

class RepellentData(Base):
    __tablename__ = 'repellent_data'
    id = Column(BIGINT, primary_key=True, index=True)
    detection_date = Column(String)
    detection_num = Column(Integer, default=0)
    detection_time = Column(String)
    re_detection_minutes = Column(BIGINT, default=0)
    repellent_device_id = Column(BIGINT, ForeignKey('repellent_device.id'))
    repellent_sound_id = Column(BIGINT, ForeignKey('repellent_sound.id'))
    detection_type = Column(Enum(DetectionTypeEnum))

    repellent_device = relationship("RepellentDevice", back_populates="repellent_data")
    repellent_sound = relationship("RepellentSound", back_populates="repellent_data")
