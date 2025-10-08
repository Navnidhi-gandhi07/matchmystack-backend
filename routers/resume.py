from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from ml.parser import parse_resume
from ml.embedder import get_embedding
from models import User

router = APIRouter(prefix="/resume")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
def upload_resume(user_id: int, file: UploadFile, db: Session = Depends(get_db)):
    parsed = parse_resume(file.file)
    embedding = get_embedding(parsed["text"])
    user = db.query(User).filter(User.id == user_id).first()
    user.resume_text = parsed["text"]
    user.resume_embedding = embedding
    db.commit()
    return {"skills": parsed["skills"], "summary": parsed["summary"]}

