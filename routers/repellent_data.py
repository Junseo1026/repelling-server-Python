from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.repellent_data import create_repellent_data, get_repellent_data, get_daily_detections, get_hourly_detections, get_main_page_data
from schemas.repellent_data import RepellentData as RepellentDataSchema, RepellentDataCreate, RepellentDataRequest
from schemas.repellent_data import *
from database import get_db

router = APIRouter()

@router.post("/", response_model=RepellentDataSchema)
def create_repellent_data_route(repellent_data: RepellentDataCreate, db: Session = Depends(get_db)):
    return create_repellent_data(db, repellent_data)

@router.get("/{data_id}", response_model=RepellentDataSchema)
def get_repellent_data_route(data_id: int, db: Session = Depends(get_db)):
    data = get_repellent_data(db, data_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.get("/daily-detections", response_model=DailyDetectionListResponse)
def get_daily_detections_route(db: Session = Depends(get_db)):
    return get_daily_detections(db)

@router.get("/hourly-detections", response_model=HourByDetectionListResponse)
def get_hourly_detections_route(db: Session = Depends(get_db)):
    return get_hourly_detections(db)

@router.get("/main-page-data", response_model=MainPageDataResponse)
def get_main_page_data_route(db: Session = Depends(get_db)):
    return get_main_page_data(db)


# @router.post("/")
# async def repellent_data(request: RepellentDataRequest, db: Session = Depends(get_db)):
#     gateway = db.query(Gateway).filter_by(serial_id=request.gatewayId).first()
#     if not gateway:
#         raise HTTPException(status_code=404, detail="Gateway not found")
#
#     db_data = RepellentData(
#         detection_date=datetime.strptime(request.timestamp, '%Y-%m-%d,%H:%M:%S'),
#         detection_num=request.detectedCount,
#         detection_time=request.timestamp.split(',')[1],
#         farm_id=gateway.id,  # gateway ID를 사용
#         member_id=gateway.member_id,  # 관련 멤버 ID를 사용
#         re_detection_minutes=5,  # 필요 시 계산
#         repellent_device_id=1,  # 필요 시 실제 데이터 사용
#         repellent_sound_id=1,  # 필요 시 실제 데이터 사용
#         detection_type=request.detectionType
#     )
#     db.add(db_data)
#     db.commit()
#     db.refresh(db_data)
#     return JSONResponse(status_code=200, content={"message": "Data created successfully"})


