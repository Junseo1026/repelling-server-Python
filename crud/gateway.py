from sqlalchemy.orm import Session
from models.gateway import Gateway

def get_gateway(db: Session, gateway_id: int):
    return db.query(Gateway).filter(Gateway.id == gateway_id).first()

def get_gateways(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Gateway).offset(skip).limit(limit).all()

def create_gateway(db: Session, gateway: Gateway):
    db.add(gateway)
    db.commit()
    db.refresh(gateway)
    return gateway

def gateway_exists_by_serial_id(db: Session, serial_id: str):
    return db.query(Gateway).filter(Gateway.serial_id == serial_id).first() is not None
