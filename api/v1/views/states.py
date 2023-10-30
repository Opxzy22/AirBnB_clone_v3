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

@app.route('/items', methods=['POST']), strict_slashes= False
def create_state():
     # Check if the request data is valid JSON
    if not request.is_json:
        return jsonify({"message": "Not a JSON"}), 400

    state_data = request.get_json()

    # Check if the 'name' key is present in the request data
    if 'name' not in state_data:
        return jsonify({"message": "Missing name"}), 400

    # Generate a new State ID
    state_id = len(data) + 1
    state = State(state_id, state_data['name'])
    data[state_id] = state.__dict__

    return jsonify(state.__dict__), 201

# Add more routes and functions for other RESTful actions (GET, PUT, DELETE) as needed

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/state/states_id>', methods=['PUT']), strict_slashes= False
def update_state(state_id):
    state = data.get(state_id)

      if state:
        state_data = request.get_json()

        # Validate if the request body is valid JSON
        if not state_data:
            return jsonify({'error': 'Not a JSON'}), 400

        # Update the State object with key-value pairs from the request data
        for key, value in state_data.items():
            if key not in ('id', 'created_at', 'updated_at'):
                state[key] = value

        return jsonify(state), 200
    return jsonify({'error': 'Item not found'}), 404

# Other RESTful API actions for State objects (e.g., GET, POST, DELETE) can be added here.

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/state/<states_id>', methods=['DELETE'])
def delete_state(state_id):
    state = data.pop(state_id, None)
    if item:
        return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
