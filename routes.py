from flask import Blueprint, jsonify
from models import Employee
from collections import defaultdict

api = Blueprint('api', __name__)

@api.route('/api/summary', methods=['GET'])
def summary():
    employees = Employee.query.all()

    data = defaultdict(lambda: {"count": 0, "total_salary": 0, "max_salary": 0, "min_salary": float("inf"), "total_age": 0})

    for emp in employees:
        stats = data[emp.department]
        stats["count"] += 1
        stats["total_salary"] += emp.salary
        stats["max_salary"] = max(stats["max_salary"], emp.salary)
        stats["min_salary"] = min(stats["min_salary"], emp.salary)
        stats["total_age"] += emp.age

    result = {
        dept: {
            "avg_salary": round(stats["total_salary"] / stats["count"], 2),
            "max_salary": stats["max_salary"],
            "min_salary": stats["min_salary"],
            "avg_age": round(stats["total_age"] / stats["count"], 1),
            "count": stats["count"]
        }
        for dept, stats in data.items()
    }

    return jsonify(result)
