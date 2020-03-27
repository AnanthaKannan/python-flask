from flask import Blueprint, jsonify, request
admin_route = Blueprint('', __name__,)

from .response import response 
import curd.curd as curd
import query.admin_qry as admin_qry

@admin_route.route('/getAllAdmin', methods=['GET'])
def getAllAdmin():
    data = curd.read(admin_qry.get_all_admin)
    return jsonify(response(data, 'GET')), 200

@admin_route.route('/adminByName/<string:name>', methods=['GET'])
def getAdminByName(name):
    value = (name,)
    data = curd.read(admin_qry.get_admin_by_name, value)
    return jsonify(response(data, 'GET')), 200

@admin_route.route('/addAdmin', methods=['POST'])
def addAdmin():
    req_data = request.get_json()
    values = (req_data['name'], req_data['address'], req_data['age'],)
    count = curd.modifi(admin_qry.add_new_admin, values)
    return response(count, 'POST'), 200
    
@admin_route.route('/adminByName/<string:name>', methods=['DELETE'])
def deleteAdminByName(name):
    value = (name,)
    count = curd.modifi(admin_qry.delete_admin_by_name, value)
    return response(count, 'DELETE'), 200

@admin_route.route('/adminById/<int:id>', methods=['PUT'])
def updateAdminById(id):
    req = request.get_json()
    value = (req['address'], id,)
    count = curd.modifi(admin_qry.update_admin_by_id, value)
    return response(count, 'PUT'), 200

@admin_route.errorhandler(Exception)
def handle_error(error):
    return {
        'error': error,
        'status':500
    },500