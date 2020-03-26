from flask import Blueprint, jsonify
admin_route = Blueprint('', __name__,)

import curd.curd as curd
import query.admin_qry as admin_qry

@admin_route.route('/getAllAdmin', methods=['GET'])
def create_store():
    # req_data = request.get_json()
    curd.read(admin_qry.get_all_admin)
    new_store = {
        'name':'anantha kannan',
        'items':[]
    }
    # stores.append(new_store), 200
    return jsonify(new_store), 404