from fastapi import APIRouter, Depends
from schemas.schemas import UserCreate
from sqlalchemy.orm import Session
from db.database import get_db
from services.create_user import create_user

router = APIRouter()

@router.post("/create-user")
async def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db,user)