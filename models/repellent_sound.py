from sqlalchemy import Column, String, Integer, BIGINT
from database import Base
from sqlalchemy.orm import relationship

class RepellentSound(Base):
    __tablename__ = 'repellent_sound'
    id = Column(BIGINT, primary_key=True, index=True)
    sound_level = Column(Integer)
    sound_name = Column(String(255))

    repellent_data = relationship("RepellentData", back_populates="repellent_sound")

