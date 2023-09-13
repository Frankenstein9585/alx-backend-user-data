#!/usr/bin/env python3
"""End-to-End Integration Testing"""
import json

import requests


def register_user(email: str, password: str) -> None:
    url = "http://localhost:5000/users"

    data = {
        "email": email,
        "password": password
    }

    response = requests.post(url, json=data)

    assert response.status_code == 200, f"Registration failed with status code {response.status_code}"
    assert response.json() == {"email": email, "message": "user created"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
