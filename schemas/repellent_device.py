from pydantic import BaseModel
from typing import Optional

class RepellentDevice(BaseModel):
    id: Optional[int]
    is_activated: bool
    is_working: bool
    farm_id: int
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    name: Optional[str] = None
    serial_id: Optional[str] = None

    class Config:
        from_attributes = True  # orm_mode 대신 from_attributes 사용
