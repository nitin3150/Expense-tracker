from db.database import get_db
from db.models import User
from sqlalchemy.orm import Session
from schemas.schemas import UserCreate
from fastapi import Depends


def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name = user.name, email = user.email)
    db.add(new_user)
    db.commit()
    print("User Created")
    return {user.name: user.email}