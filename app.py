from flask import Flask, request
from flask_restful import Resource, Api
import mysql.connector



app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return { 'student':name}

api.add_resource(Student, '/student/<string:name>')
app.run(debug=True, port=5000)


# mongodb://SreeAnanthaKannan:qwe$7500@ds163354.mlab.com:63354/testt