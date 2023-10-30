#!/usr/bin/python3

"""
Create a new view for State objects that handles all default RESTFul API actions:
"""
from flask import Flask, request, jsonify

app = Flask(__name)

# Sample data to simulate a database
data = {
    1: {'id': 1, 'name': 'Item 1'},
    2: {'id': 2, 'name': 'Item 2'},
    3: {'id': 3, 'name': 'Item 3'},
}

class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# RESTful API to handle CRUD operations for items
@app.route('/items', methods=['GET'])
def get_items():
    items = [item.__dict__ for item in data.values()]
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = data.get(item_id)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def create_item():
    item_data = request.get_json()
    item_id = len(data) + 1
    item = Item(item_id, item_data['name'])
    data[item_id] = item.__dict__
    return jsonify(item.__dict__), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = data.get(item_id)
    if item:
        item_data = request.get_json()
        item.name = item_data['name']
        return jsonify(item.__dict__)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = data.pop(item_id, None)
    if item:
        return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
