from flask import Blueprint, jsonify, request

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(Exception)
def handle_error(error):
    response = {
        'error': str(error),
        'status': 400
    }
    return jsonify(response),400

@errors.app_errorhandler(404)
def not_fount(error=None):
    response = {
        'status':404,
        'message': 'Not found ' + request.url
    }
    return jsonify(response), 404