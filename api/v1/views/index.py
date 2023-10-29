#!/usr/bin/python3
"""create a route for the status"""
from api.v1.views import app_views
from flask import jsonify
from model import storage


@app_views.route('/status', methods=['get'])
def get_status():
    status = ["status": "ok"]
    return jsonify(status)


@app_views.route('/stats', strict_slashes=False)
def get_stat():
    stats = {}
    classes = {
            "amenities": "Amenity",
            "states": "State",
            "places": "Place",
            "reviews": "Review",
            "users": "User",
            "cities": "City"
            }
    for class_name, class_key in classes.items():
        count = storage.count(class_name)
        stats[class_key] = count
    return jsonify(stat)
