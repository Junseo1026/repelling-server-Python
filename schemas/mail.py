from enum import Enum
from pydantic import BaseModel

class MailCodeEnum(str, Enum):
    REGISTRATION = "REGISTRATION"
    PASSWORD_RESET = "PASSWORD_RESET"

class MailMessage(BaseModel):
    to: str
    subject: str
    text: str

    class Config:
        from_attributes = True