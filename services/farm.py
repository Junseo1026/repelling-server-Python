from sqlalchemy.orm import Session
from crud import farm as farm_crud
from schemas.farm import FarmRequest

def create_farm(db: Session, request: FarmRequest):
    return farm_crud.create_farm(db, request)

def get_farms(db: Session):
    return farm_crud.get_farms(db)

def get_farm(db: Session, farm_id: int):
    return farm_crud.get_farm(db, farm_id)

def get_farms_by_member_id(db: Session, member_id: int):
    return farm_crud.get_farms_by_member_id(db, member_id)
