#!/usr/bin/env python3
"""This file contains the Auth Class"""
import os

from flask import request
from typing import List, TypeVar

from models.user import User
import re


class Auth:
    """The Auth Class"""

    def __init__(self):
        """Initialize the class"""
        ...

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This returns None for now"""
        if not path:
            return True
        if not path.endswith('/'):
            path += '/'
        if not excluded_paths or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        for item in excluded_paths:
            if item.endswith('*'):
                pattern = item.split('*')[0]
                if re.match(r"{}.*".format(pattern), path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """This returns None for now"""
        if not request:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """This returns None for now"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if not request:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME'))
