#!/usr/bin/env python3
"""auth.py for Authentication"""

from bcrypt import hashpw, gensalt, checkpw
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a User"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'User {user.email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Validates login details"""
        try:
            user = self._db.find_user_by(email=email)
            if checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Finds a user based on their session_id"""
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys the user session"""
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
        except NoResultFound:
            return
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Generates a password reset token"""
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            user.reset_token = reset_token
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates a users password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user_id=user.id,
                                 hashed_password=hashed_password,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt"""
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    return str(uuid.uuid4())
