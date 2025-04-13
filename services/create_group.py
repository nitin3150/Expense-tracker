from db.database import get_db
from db.models import Group

db = get_db()

def create_group(name, created_by):
    new_group = Group(name = name, created_by = created_by)
    db.add(new_group)
    db.commit()
    print("Group Created")