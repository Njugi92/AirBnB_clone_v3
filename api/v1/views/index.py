#!/usr/bin/python3
'''The api status'''
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def returnstuff():
    '''To return stuff'''
    return jsonify({'status' : 'OK'})


@app_views.route('/stats', methods=['GET'])
def stuff():
    '''JSON Responses'''
    todos = {'states': State, 'users': User,
             'amenities': Amenity, 'cities': City,
             'places': Place, 'reviews': Review}
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)
