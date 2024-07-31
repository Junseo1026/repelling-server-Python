from sqlalchemy.orm import Session
from models.repellent_data import RepellentData
from schemas.repellent_data import RepellentDataCreate

def get_repellent_data(db: Session, data_id: int):
    return db.query(RepellentData).filter(RepellentData.id == data_id).first()

def get_repellent_data_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RepellentData).offset(skip).limit(limit).all()

def create_repellent_data(db: Session, repellent_data: RepellentDataCreate):
    db_repellent_data = RepellentData(**repellent_data.dict())
    db.add(db_repellent_data)
    db.commit()
    db.refresh(db_repellent_data)
    return db_repellent_data

# Custom methods based on RepellentDataRepositoryCustom.java
def get_daily_detections(db: Session):
    # Implement the logic to get daily detections
    pass

def get_hourly_detections(db: Session):
    # Implement the logic to get hourly detections
    pass

def get_main_page_data(db: Session):
    # Implement the logic to get main page data
    pass
