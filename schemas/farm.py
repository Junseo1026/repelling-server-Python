from pydantic import BaseModel
from typing import Optional
from enum import Enum
from typing import List

class FarmTypeEnum(str, Enum):
    GINSENG_FIELD = "GINSENG_FIELD"
    ONCHARD = "ONCHARD"
    RICE_FARM = "RICE_FARM"

class FarmRequest(BaseModel):
    gateway_id: Optional[int]
    member_id: Optional[int]
    address: Optional[str]
    farm_type: Optional[FarmTypeEnum]
    name: Optional[str]

    class Config:
        from_attributes = True
class FarmResponse(BaseModel):
    id: int
    gateway_id: int
    member_id: int
    address: str
    farm_type: FarmTypeEnum
    name: str

    class Config:
        from_attributes = True

class FarmListResponse(BaseModel):
    farms: List[FarmResponse]

    class Config:
        from_attributes = True
