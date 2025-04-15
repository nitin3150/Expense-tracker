from db.database import get_db
from db.models import User
from sqlalchemy.orm import Session
from schemas.schemas import UserCreate

# db = get_db()

def create_user(db: Session, user: UserCreate):
    new_user = User(name = user.name, email = user.email)
    db.add(new_user)
    db.commit()
    print("User Created")
    return new_user