#!/usr/bin/env python3
"""A Flask Application"""
from typing import Tuple

from auth import Auth
from flask import Flask, jsonify, request, Response

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """returns a JSON Payload"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> Response | tuple[Response, int]:
    """Route for registering users"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({'email': new_user.email, 'message': 'user created'})
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
