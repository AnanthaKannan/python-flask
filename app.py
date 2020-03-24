from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name':'My wonderful store',
        'items':[
            {
                'name':'my item',
                'price':44.3
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    req_data = request.get_json()
    new_store = {
        'name':req_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store_by_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

@app.route('/store')
def get_store():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    req_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': req_data['name'],
                'price': req_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Item not found'})

app.run(port=5000, debug=True)