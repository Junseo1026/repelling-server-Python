from sqlalchemy.orm import Session
from schemas.repellent_data import RepellentDataRequest, RepellentDataCreate, RepellentData as RepellentDataSchema
from crud import repellent_data as repellent_data_crud

def create_repellent_data(db: Session, request: RepellentDataRequest):
    new_data = RepellentData(
        detection_date=request.detection_date,
        detection_num=request.detection_num,
        detection_time=request.detection_time,
        re_detection_minutes=request.re_detection_minutes,
        repellent_device_id=request.repellent_device_id,
        repellent_sound_id=request.repellent_sound_id,
        detection_type=request.detection_type
    )
    return repellent_data_crud.create_repellent_data(db, new_data)

def get_repellent_data(db: Session, data_id: int):
    return repellent_data_crud.get_repellent_data(db, data_id)

def get_daily_detections(db: Session):
    return repellent_data_crud.get_daily_detections(db)

def get_hourly_detections(db: Session):
    return repellent_data_crud.get_hourly_detections(db)

def get_main_page_data(db: Session):
    return repellent_data_crud.get_main_page_data(db)

def register_repellent_data(db: Session, repellent_data: RepellentDataCreate) -> RepellentDataSchema:
    return repellent_data_crud.create_repellent_data(db, repellent_data)
