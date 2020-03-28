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

@admin_route.route('/adminByid/<string:id>', methods=['DELETE'])
def adminByid(id):
    admin = Admin.objects(id=id).delete()
    return response( str(admin), 'DELETE'), 200

@admin_route.route('/adminById/<string:id>', methods=['PUT'])
def updateAdminById(id):
    body = request.get_json()
    admin = Admin.objects(id=id).update(**body)
    return response(str(admin), 'PUT')
