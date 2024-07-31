from pydantic import BaseModel, EmailStr

class CertificationNumberResponse(BaseModel):
    certification_number: str

    class Config:
        from_attributes = True  # orm_mode 대신 from_attributes 사용

class FindIdResponse(BaseModel):
    login_id: str

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    login_id: str
    password: str

    class Config:
        from_attributes = True

class LoginResponse(BaseModel):
    token: str

    class Config:
        from_attributes = True

class RegisterRequest(BaseModel):
    email: str
    login_id: str
    name: str
    password: str

    class Config:
        from_attributes = True

class MemberBase(BaseModel):
    email: EmailStr
    login_id: str
    name: str

class MemberCreate(MemberBase):
    password: str

class Member(MemberBase):
    id: int

    class Config:
        from_attributes = True
