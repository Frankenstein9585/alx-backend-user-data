#!/usr/bin/env python3
"""End-to-End Integration Testing"""
import json

import requests


def register_user(email: str, password: str) -> None:
    """Tests the Register User"""
    url = "http://localhost:5000/users"
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, data=data)

    assert response.status_code == 200, \
        f"Registration failed with status code {response.status_code}"
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Tests Login route"""
    url = 'http://localhost:5000/sessions'
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, data=data)

    assert response.status_code == 401


def profile_unlogged() -> None:
    """Test Profile while user isn't logged in"""
    url = 'http://localhost:5000/profile'
    response = requests.get(url)

    assert response.status_code == 403


def log_in(email: str, password: str) -> str:
    """Tests the login route"""
    url = 'http://localhost:5000/sessions'
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(url, data=data)

    assert response.status_code == 200, (
        'Login failed with error code {}'.format(response.status_code))
    assert response.json() == {'email': email, 'message': 'logged in'}

    return response.cookies.get('session_id')


def profile_logged(session_id: str) -> None:
    """Tests the profile route while the user is logged in"""
    url = 'http://localhost:5000/profile'

    data = {
        'session_id': session_id
    }
    response = requests.get(url, cookies=data)

    assert response.status_code == 200
    assert response.json().get('email')


def log_out(session_id: str) -> None:
    """Tests the logout route"""
    url = 'http://localhost:5000/sessions'
    data = {
        'session_id': session_id
    }

    response = requests.delete(url, cookies=data)

    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """Tests the route that generates rest_tokens"""
    url = 'http://localhost:5000/reset_password'
    data = {
        'email': email
    }

    response = requests.post(url, data=data)

    assert response.status_code == 200
    assert response.json().get('email')
    assert response.json().get('reset_token')
    return response.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests the route for updating passwords"""
    url = 'http://localhost:5000/reset_password'
    data = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    }

    response = requests.put(url, data=data)

    assert response.status_code == 200, (
        'Failed with error code: {}'.format(response.status_code))
    assert response.json() == {'email': email, 'message': 'Password updated'}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
