from flask import Blueprint, jsonify, request
admin_route = Blueprint('', __name__,)

from .response import response 
from database.models import Admin

@admin_route.route('/getAllAdmin', methods=['GET'])
def getAllAdmin():
    admins = Admin.objects({})
    return jsonify(response(admins, 'GET')), 200

@admin_route.route('/adminByName/<string:name>', methods=['GET'])
def getAdminByName(name):
    admins = Admin.objects(name=name)
    return jsonify(response(admins, 'GET')), 200

@admin_route.route('/addAdmin', methods=['POST'])
def addAdmin():
    body = request.get_json()
    admin = Admin(**body).save()
    id = admin.id
    return response( str(id), 'POST'), 200

@admin_route.route('/adminByName/<string:name>', methods=['DELETE'])
def deleteAdminByName(name):
    admin = Admin.objects({})
    return response( str(admin), 'DELETE'), 200

@admin_route.route('/adminById/<int:id>', methods=['PUT'])
def updateAdminById(id):
    req = request.get_json(_id=id).delete_one()
    value = (req['address'], id,)
    count = curd.modifi(admin_qry.update_admin_by_id, value)
    return response(count, 'PUT'), 200

