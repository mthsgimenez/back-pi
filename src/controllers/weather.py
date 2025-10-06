from services import weather
from flask import Blueprint, jsonify

weather_bp = Blueprint('weather_bp', __name__)

@weather_bp.route('/', methods=['GET'])
def weather_get():
    return jsonify(weather.getCurrentWeather())