from flask import Flask, render_template
from db import db
from models import Employee
from routes import api
from generate_data import generate_employees
from flask_swagger_ui import get_swaggerui_blueprint
import os

# Config class
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///employees.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Create app
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)



# Register API blueprint
app.register_blueprint(api)

# Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# @app.before_first_request
# def setup():
#     db.create_all()
#     if not Employee.query.first():
#         generate_employees(200)

  
@app.route('/')
def dashboard():
    employees = Employee.query.all()
    return render_template("dashboard.html", employees=employees)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database and tables created.")
    app.run(debug=True, port=5000)


