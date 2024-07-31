from sqlalchemy.orm import Session
from crud import gateway as gateway_crud
from models.gateway import Gateway

def create_gateway(db: Session, gateway: Gateway):
    return gateway_crud.create_gateway(db, gateway)

def get_gateway(db: Session, gateway_id: int):
    return gateway_crud.get_gateway(db, gateway_id)

def gateway_exists_by_serial_id(db: Session, serial_id: str):
    return gateway_crud.gateway_exists_by_serial_id(db, serial_id)
