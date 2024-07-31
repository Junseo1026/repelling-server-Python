from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import repellent_device as repellent_device_service
from schemas.repellent_device import RepellentDevice
from database import get_db

router = APIRouter()

@router.post("/", response_model=RepellentDevice)
def create_repellent_device(device: RepellentDevice, db: Session = Depends(get_db)):
    return repellent_device_service.create_repellent_device(db, device)

@router.get("/{device_id}", response_model=RepellentDevice)
def get_repellent_device(device_id: int, db: Session = Depends(get_db)):
    device = repellent_device_service.get_repellent_device(db, device_id)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@router.get("/serial/{serial_id}", response_model=RepellentDevice)
def get_repellent_device_by_serial_id(serial_id: str, db: Session = Depends(get_db)):
    device = repellent_device_service.get_repellent_device_by_serial_id(db, serial_id)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device
