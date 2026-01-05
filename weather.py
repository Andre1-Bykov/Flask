from flask import Blueprint, request, jsonify
from datetime import datetime
import random

weather_bp = Blueprint(
    "weather",
    __name__,
    url_prefix="/api/weather"
)

# 1. Простой динамический маршрут
@weather_bp.route("/hello/<name>")
def hello(name):
    return f"Привет, {name}!"

# 2. Query-параметры
@weather_bp.route("/city")
def city():
    city = request.args.get("city", "не указан")
    return {"city": city}

# 3. Динамика (рандом + время)
@weather_bp.route("/now")
def now():
    return jsonify({
        "time": datetime.now().strftime("%H:%M:%S"),
        "temperature": random.randint(-10, 30)
    })
