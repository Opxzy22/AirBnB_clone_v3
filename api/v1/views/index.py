#!/usr/bin/python3
"""create a route for the status"""
from api.v1.views import app_views
from flask import jsonify
from model import storage


@app_views.route('/status', methods=['get'])
def get_status():
    """ configures the status route"""

    status = ["status": "ok"]
    return jsonify(status)


@app_views.route('/stats', strict_slashes=False)
def get_stat():
    """ return the stats of the objects"""

    classes = {
            "amenities": "Amenity",
            "states": "State",
            "places": "Place",
            "reviews": "Review",
            "users": "User",
            "cities": "City"
            }
    stats = {
            att: storage.count(cls)
            for att, cls in classes.items()
            }

    return jsonify(stats)
