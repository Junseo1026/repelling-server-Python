from sqlalchemy.orm import Session
from models.repellent_sound import RepellentSound

def get_repellent_sound(db: Session, sound_id: int):
    return db.query(RepellentSound).filter(RepellentSound.id == sound_id).first()

def get_repellent_sounds(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RepellentSound).offset(skip).limit(limit).all()

def create_repellent_sound(db: Session, sound: RepellentSound):
    db.add(sound)
    db.commit()
    db.refresh(sound)
    return sound
