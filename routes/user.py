from fastapi import APIRouter, Depends,Form
from schemas.schemas import UserCreate
from sqlalchemy.orm import Session
from db.database import get_db
from services.create_user import create_user

router = APIRouter()

# @router.post("/create-user")
# async def add_user(user: UserCreate, db: Session = Depends(get_db)):
#     return create_user(user,db)

@router.post("/create-user")
async def add_user(
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    user = UserCreate(name=name, email=email)  # Create a Pydantic model manually
    return create_user(user, db)