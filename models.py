from db import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    department = db.Column(db.String(50))
    salary = db.Column(db.Float)
    age = db.Column(db.Integer)
    join_date = db.Column(db.Date)
