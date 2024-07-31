from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class DetectionTypeEnum(str, Enum):
    BIRD = "BIRD"
    PIG = "PIG"
    PIR = "PIR"


class DayByDetection(BaseModel):
    date: str
    detection_count: int

    class Config:
        from_attributes = True


class DailyDetectionListResponse(BaseModel):
    day_by_detections: List[DayByDetection]

    class Config:
        from_attributes = True


class HourByDetection(BaseModel):
    hour: str
    detection_count: int

    class Config:
        from_attributes = True


class HourByDetectionListResponse(BaseModel):
    hour_by_detections: List[HourByDetection]

    class Config:
        from_attributes = True


class MainPageDataResponse(BaseModel):
    total_detections_today: int
    total_detections_this_week: int
    total_detections_this_month: int

    class Config:
        from_attributes = True


class ReDetectionMinutesAndRepellentSoundResponse(BaseModel):
    re_detection_minutes: int
    repellent_sound_name: str

    class Config:
        from_attributes = True


class RepellentDataRequest(BaseModel):
    detection_time: datetime
    detection_type: str
    repellent_device_id: Optional[int]
    repellent_sound_id: Optional[int]

    class Config:
        from_attributes = True


class RepellentDataBase(BaseModel):
    detection_date: str
    detection_num: int
    detection_time: str
    re_detection_minutes: int
    repellent_device_id: int
    repellent_sound_id: int
    detection_type: DetectionTypeEnum


class RepellentDataCreate(RepellentDataBase):
    pass


class RepellentData(RepellentDataBase):
    id: int

    class Config:
        from_attributes = True
