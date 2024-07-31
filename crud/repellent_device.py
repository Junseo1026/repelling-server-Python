from sqlalchemy.orm import Session
from models.repellent_device import RepellentDevice

def get_repellent_device(db: Session, device_id: int):
    return db.query(RepellentDevice).filter(RepellentDevice.id == device_id).first()

def get_repellent_devices(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RepellentDevice).offset(skip).limit(limit).all()

def get_repellent_device_by_serial_id(db: Session, serial_id: str):
    return db.query(RepellentDevice).filter(RepellentDevice.serial_id == serial_id).first()

def create_repellent_device(db: Session, device: RepellentDevice):
    db.add(device)
    db.commit()
    db.refresh(device)
    return device
