#!/usr/bin/env python3
"""This file contains the SessionAuth Class"""
import uuid
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """The SessionAuth Class"""
    user_id_by_session_id = dict()

    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """Creates a session and stores the session ID in a dictionary"""
        if not user_id or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        if not session_id or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns a user instance based on a cookie value"""
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes the user session"""
        if not request:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        if not self.user_id_for_session_id(session_id):
            return False
        self.user_id_by_session_id.pop(session_id)
        return True
