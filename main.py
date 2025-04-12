from db.database import SessionLocal
from db.models import User, Expense

db = SessionLocal()

# Add a user
new_user = User(name="Nitin",email="nitingoyal6742@gmail.com")
db.add(new_user)
db.commit()

# Add an expense
expense = Expense(amount=99.99, description="Dinner", payer_id=new_user.id)
db.add(expense)
db.commit()

# Query expenses
expenses = db.query(Expense).filter(Expense.user_id == new_user.id).all()
for exp in expenses:
    print(exp.description, exp.amount)

db.close()