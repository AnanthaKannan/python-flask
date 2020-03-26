from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'secretkey'
api = Api(app)

Data = []

class HelloWorld(Resource):
    def __init__(self):
        pass
    def get(self, name):
        for x in Data:
            if x['name'] == name:
                return x, 200
        return { 'name':None }, 404

    def post(self, name):
        temp = {'name':name}
        Data.append(temp)
        return temp, 201

    def delete(self, name):
        for ind, x in enumerate(Data):
            if x['name'] == name:
                temp = Data.pop(ind)
                return { 'Note':'Deleted' }, 200
        return { 'msg':'User name not there' }, 404


api.add_resource(HelloWorld, '/name/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)