from fastapi import APIRouter, Depends
from services.mail import send_mail
from schemas.mail import MailMessage

router = APIRouter()

@router.post("/send")
def send_mail_endpoint(mail_message: MailMessage):
    send_mail(mail_message)
    return {"message": "Mail sent successfully"}
