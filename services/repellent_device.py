from sqlalchemy.orm import Session
from crud import repellent_device as repellent_device_crud
from models.repellent_device import RepellentDevice

def create_repellent_device(db: Session, device: RepellentDevice):
    return repellent_device_crud.create_repellent_device(db, device)

def get_repellent_device(db: Session, device_id: int):
    return repellent_device_crud.get_repellent_device(db, device_id)

def get_repellent_device_by_serial_id(db: Session, serial_id: str):
    return repellent_device_crud.get_repellent_device_by_serial_id(db, serial_id)
