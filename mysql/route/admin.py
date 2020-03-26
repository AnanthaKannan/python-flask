from flask import Blueprint, jsonify, request
admin_route = Blueprint('', __name__,)

import curd.curd as curd
import query.admin_qry as admin_qry

@admin_route.route('/getAllAdmin', methods=['GET'])
def getAllAdmin():
    data = curd.read(admin_qry.get_all_admin)
    resutl = {
        'data':data,
        'status':200
    }
    # stores.append(new_store), 200
    return jsonify(resutl), 200

@admin_route.route('/adminByName/<string:name>', methods=['GET'])
def getAdminByName(name):
    print(name)
    # req_data = request.get_json()
    value = (name,)
    data = curd.read(admin_qry.get_admin_by_name, value)
    resutl = {
        'data':data,
        'status':200
    }
    return jsonify(resutl), 200

@admin_route.route('/addAdmin', methods=['POST'])
def addAdmin():
    req_data = request.get_json()
    values = (req_data['name'], req_data['address'], req_data['age'],)
    # values = ('hello', 'mmbai', 45,)
    count = curd.modifi(admin_qry.add_new_admin, values)
    result = {
        'data':count,
        'status':200,
        'message': 'Sucessfully inserted'
    }
    return result

@admin_route.route('/adminByName/<string:name>', methods=['DELETE'])
def deleteAdminByName(name):
    value = (name,)
    count = curd.modifi(admin_qry.delete_admin_by_name, value)
    result = {
        'data':count,
        'status':200,
        'message': 'Sucessfully deleted.'
    }
    return result