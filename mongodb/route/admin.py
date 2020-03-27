from flask import Blueprint, jsonify, request
admin_route = Blueprint('', __name__,)

from .response import response 
from database.models import Admin

@admin_route.route('/getAllAdmin', methods=['GET'])
def getAllAdmin():
    admins = Admin.find_one()
    return jsonify(response(admins, 'GET')), 200

@admin_route.route('/adminByName/<string:name>', methods=['GET'])
def getAdminByName(name):
    value = (name,)
    data = curd.read(admin_qry.get_admin_by_name, value)
    return jsonify(response(data, 'GET')), 200

@admin_route.route('/addAdmin', methods=['POST'])
def addAdmin():
    body = request.get_json()
    admin = Admin(**body).save()
    id = admin.id
    return response( str(id), 'POST'), 200

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

