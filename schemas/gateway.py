from pydantic import BaseModel

class Gateway(BaseModel):
    id: int
    name: str
    serial_id: str
class SerialIdExistResponse(BaseModel):
    exists: bool

    class Config:
        from_attributes = True  # orm_mode 대신 from_attributes 사용
