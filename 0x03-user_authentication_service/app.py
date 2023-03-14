#!/usr/bin/env python3
'''
A basic Flask application with auth
'''

from flask import Flask, jsonify, request, abort
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    '''
    Home route
    '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    '''authenticates users
    '''
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    try:
        AUTH.register_user(email, password)
        return jsonify(
            {"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    '''Defines login route
    '''
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    resp = jsonify({"email": email, "message": "logged in"})
    resp.set_cookie('session_id', session_id)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
