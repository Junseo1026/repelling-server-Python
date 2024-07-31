from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from schemas.mail import MailMessage

conf = ConnectionConfig(
    MAIL_USERNAME = "your-email@example.com",
    MAIL_PASSWORD = "your-password",
    MAIL_FROM = "your-email@example.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

fast_mail = FastMail(conf)

def send_mail(mail_message: MailMessage):
    message = MessageSchema(
        subject=mail_message.subject,
        recipients=[mail_message.to],
        body=mail_message.text,
        subtype="plain"
    )

    fast_mail-send_mail(message)
