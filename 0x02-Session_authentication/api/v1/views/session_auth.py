#!/usr/bin/env python3
"""This file contains a routes that handle Session Authentication"""
import os

from api.v1.views import app_views
from flask import request, jsonify
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles Session Authentication"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == '':
        return jsonify({'error': 'email missing'}), 400
    if not password or password == '':
        return jsonify({'error': 'password missing'}), 400

    user = User.search({'email': email})
    if len(user) != 0:
        user = user[0]
    else:
        user = None
    if not user:
        return jsonify({'error': 'no user found for this email'}), 400
    if not user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401

    from api.v1.app import auth
    _my_session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(os.getenv('SESSION_NAME'), _my_session_id)
    return response
