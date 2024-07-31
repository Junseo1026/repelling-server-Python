from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from services import farm as farm_service
from schemas.farm import FarmRequest, FarmResponse, FarmListResponse
from database import get_db
from models.farm import *
from models.repellent_device import *
from models.repellent_device import RepellentDevice
from typing import List

router = APIRouter()

@router.post("/", response_model=FarmResponse)
def create_farm(request: FarmRequest, db: Session = Depends(get_db)):
    return farm_service.create_farm(db, request)

@router.get("/", response_model=FarmListResponse)
def get_farms(db: Session = Depends(get_db)):
    farms = farm_service.get_farms(db)
    return FarmListResponse(farms=farms)

@router.get("/{farm_id}", response_model=FarmResponse)
def get_farm(farm_id: int, db: Session = Depends(get_db)):
    farm = farm_service.get_farm(db, farm_id)
    if farm is None:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm

@router.get("/member/{member_id}", response_model=FarmListResponse)
def get_farms_by_member_id(member_id: int, db: Session = Depends(get_db)):
    farms = farm_service.get_farms_by_member_id(db, member_id)
    return FarmListResponse(farms=farms)

@router.get("/setting/list", response_model=FarmListResponse)
def get_farm_setting_list(db: Session = Depends(get_db)):
    farms = db.query(Farm).all()
    farm_responses = []
    for farm in farms:
        device_count = db.query(RepellentDevice).filter(RepellentDevice.farm_id == farm.id).count()  # 모델 클래스 사용
        farm_response = FarmResponse(
            id=farm.id,
            gateway_id=farm.gateway_id,
            member_id=farm.member_id,
            address=farm.address,
            farm_type=farm.farm_type,
            name=farm.name,
            device_count = device_count
        )
        farm_responses.append(farm_response)
    return FarmListResponse(farms=farm_responses)

# @router.get("/setting/list", response_model=FarmListResponse)
# def get_farm_setting_list(db: Session = Depends(get_db)):
#     farms = db.query(Farm).all()
#     farm_settings = []
#
#     for farm in farms:
#         device_count = db.query(RepellentDevice).filter(RepellentDevice.farm_id == farm.id).count()  # 모델 클래스 사용
#         farm_setting = {
#             "farm_id": farm.id,
#             "device_count": device_count
#         }
#         farm_settings.append(farm_setting)
#
#     return farm_settings

# @router.get("/setting/list")
# async def get_farm_setting_list(authorization: str = Header(None), db: Session = Depends(get_db)):
#     farms = db.query(
#         Farm.id.label("farmId"),
#         Farm.name.label("farmName"),
#         Farm.address.label("farmAddress")
#     ).all()
#
#     farm_responses = []
#     for farm in farms:
#         device_count = db.query(repellent_device).filter(RepellentDevice.farm_id == farm.farmId).count()
#         farm_response = FarmResponse(
#             farmId=farm.farmId,
#             farmName=farm.farmName,
#             deviceCount=device_count,
#             farmAddress=farm.farmAddress
#         )
#         farm_responses.append(farm_response)
#
#     return farm_responses