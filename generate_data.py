from faker import Faker
from models import Employee
from db import db
import random

fake = Faker()
DEPARTMENTS = ['Engineering', 'HR', 'Sales', 'Marketing', 'Finance']

def generate_employees(n=100):
    for _ in range(n):
        emp = Employee(
            name=fake.name(),
            department=random.choice(DEPARTMENTS),
            salary=round(random.uniform(30000, 150000), 2),
            age=random.randint(22, 65),
            join_date=fake.date_between(start_date='-10y', end_date='today')
        )
        db.session.add(emp)
    db.session.commit()
