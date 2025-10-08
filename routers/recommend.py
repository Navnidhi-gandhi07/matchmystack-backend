from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import User
from sqlalchemy import text

router = APIRouter(prefix="/recommend")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}")
def recommend(user_id: int, db: Session = Depends(get_db)):
    query = text("""
        SELECT id, name, role, bio
        FROM users
        WHERE id != :uid AND resume_embedding IS NOT NULL
        ORDER BY resume_embedding <=> (SELECT resume_embedding FROM users WHERE id = :uid)
        LIMIT 5;
    """)
    res = db.execute(query, {"uid": user_id})
    return [dict(r) for r in res]

