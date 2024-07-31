from sqlalchemy.orm import Session
from models.farm import Farm
from schemas.farm import FarmRequest, FarmResponse
from schemas.repellent_device import RepellentDevice
def get_farm(db: Session, farm_id: int):
    return db.query(Farm).filter(Farm.id == farm_id).first()

def get_farms(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Farm).offset(skip).limit(limit).all()

def get_farms_by_member_id(db: Session, member_id: int):
    return db.query(Farm).filter(Farm.member_id == member_id).all()

def create_farm(db: Session, farm: FarmRequest):
    db_farm = Farm(**farm.dict())
    db.add(db_farm)
    db.commit()
    db.refresh(db_farm)
    return db_farm

def get_farm_setting_list(db: Session):
    farms = db.query(
        Farm.id.label("farmId"),
        Farm.name.label("farmName"),
        Farm.address.label("farmAddress")
    ).all()

    farm_responses = []
    for farm in farms:
        device_count = db.query(RepellentDevice).filter(RepellentDevice.farm_id == farm.farmId).count()
        farm_response = FarmResponse(
            farmId=farm.farmId,
            farmName=farm.farmName,
            deviceCount=device_count,
            farmAddress=farm.farmAddress
        )
        farm_responses.append(farm_response)

    return farm_responses