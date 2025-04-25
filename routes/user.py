from fastapi import APIRouter, Depends,Form
from schemas.schemas import UserCreate,UserLogin
from sqlalchemy.orm import Session
from db.database import get_db
from services.create_user import create_user
from services.user_login import user_login

router = APIRouter()

@router.post("/create-user")
async def add_user(
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    user = UserCreate(name=name, email=email)
    return create_user(user, db)

@router.get("/login")
async def get_user(user:UserLogin, db:Session = Depends(get_db)):
    return user_login(user,db)