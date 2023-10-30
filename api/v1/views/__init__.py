#!/usr/bin/python3
"""initialising the app"""
from flask import Flask, Blueprint
from api.v1.views import app_views
from api.v1.views.index import *

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
