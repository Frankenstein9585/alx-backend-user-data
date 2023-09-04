#!/usr/bin/env python3
"""This file contains the Auth Class"""
from flask import request
from typing import List, TypeVar

from models.user import User


class Auth:
    """The Auth Class"""

    def __init__(self):
        """Initialize the class"""
        ...

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This returns None for now"""
        return False

    def authorization_header(self, request=None) -> str:
        """This returns None for now"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """This returns None for now"""
        return None
