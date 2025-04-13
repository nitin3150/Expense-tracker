from db.database import get_db
from db.models import User

db = get_db()

def create_user(name,email):
    new_user = User(name = name, email = email)
    db.add(new_user)
    db.commit()
    print("User Created")