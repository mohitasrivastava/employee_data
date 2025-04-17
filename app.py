from flask import Flask, render_template
from db import db
from models import Employee
from routes import api
from generate_data import generate_employees
# from flask_swagger_ui import get_swaggerui_blueprint
import os

# Config class
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///employees.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Create app
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)





@app.route('/')
def dashboard():
    # return render_template("dashboard.html")   
    return "Helo" 

# Create DB tables
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database and tables created.")

