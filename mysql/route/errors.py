from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(Exception)
def handle_error(error):
    response = {
        'error': str(error),
        'status': 400
    }
    return jsonify(response),400