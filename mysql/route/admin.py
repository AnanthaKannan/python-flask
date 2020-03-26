from flask import Blueprint, jsonify
admin_route = Blueprint('', __name__,)

@admin_route.route('/store', methods=['GET'])
def create_store():
    # req_data = request.get_json()
    new_store = {
        'name':'anantha kannan',
        'items':[]
    }
    # stores.append(new_store), 200
    return jsonify(new_store), 404