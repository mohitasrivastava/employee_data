
from app import app, db
from models import Employee
from generate_data import generate_employees

with app.app_context():
    if not Employee.query.first():
        generate_employees(200)
        print("✅ Synthetic employee data inserted.")
    else:
        print("ℹ️ Employee table already has data.")
