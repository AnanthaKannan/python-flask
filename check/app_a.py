from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

Data = []

class HelloWorld(Resource):
    def __init__(self):
        pass
    def get(self, name):
        for x in Data:
            if x['name'] == name:
                return x
        return { 'name':None }

    def post(self, name):
        temp = {'name':name}
        Data.append(temp)
        return temp    

    def delete(self, name):
        for ind, x in enumerate(Data):
            if x['name'] == name:
                temp = Data.pop(ind)
                return { 'Note':'Deleted' }
        return { 'msg':'User name not there' }


api.add_resource(HelloWorld, '/name/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)