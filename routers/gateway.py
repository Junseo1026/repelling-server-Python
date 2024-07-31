from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import gateway as gateway_service
from schemas.gateway import Gateway, SerialIdExistResponse
from database import get_db

router = APIRouter()

@router.post("/", response_model=Gateway)
def create_gateway(gateway: Gateway, db: Session = Depends(get_db)):
    return gateway_service.create_gateway(db, gateway)

@router.get("/{gateway_id}", response_model=Gateway)
def get_gateway(gateway_id: int, db: Session = Depends(get_db)):
    gateway = gateway_service.get_gateway(db, gateway_id)
    if gateway is None:
        raise HTTPException(status_code=404, detail="Gateway not found")
    return gateway

@router.get("/exists/{serial_id}", response_model=SerialIdExistResponse)
def gateway_exists_by_serial_id(serial_id: str, db: Session = Depends(get_db)):
    exists = gateway_service.gateway_exists_by_serial_id(db, serial_id)
    return SerialIdExistResponse(exists=exists)
