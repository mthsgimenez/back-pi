from flask import Blueprint, jsonify

recommendations_bp = Blueprint('recommendations', __name__)

@recommendations_bp.route('/', methods=['GET'])
def recommendations_get():
    return jsonify({ 'teste': 'fasfasf' })