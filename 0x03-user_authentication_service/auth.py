#!/usr/bin/env python3
"""auth.py for Authentication"""
from bcrypt import hashpw, gensalt
from sqlalchemy.exc import NoResultFound

from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a User"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt"""
    return hashpw(password.encode(), gensalt())
