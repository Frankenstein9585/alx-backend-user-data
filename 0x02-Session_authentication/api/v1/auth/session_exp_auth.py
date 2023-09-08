#!/usr/bin/env python3
"""This file contains the SessionExpAuth Class"""
import os
from datetime import datetime, timedelta

from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """The SessionExpAuth Class"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.session_duration = int(os.getenv('SESSION_DURATION', 0))

    def create_session(self, user_id=None):
        """Overloads SessionAuth.create_session()"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_dictionary = dict()
        session_dictionary['user_id'] = user_id
        session_dictionary['created_at'] = datetime.now()
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Overloads SessionAuth.user_id_for_session_id()"""
        if not session_id or session_id not in self.user_id_by_session_id:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]['user_id']
        if 'created_at' not in self.user_id_by_session_id[session_id]:
            return None
        time = timedelta(seconds=self.session_duration)
        if ((time + self.user_id_by_session_id[session_id]['created_at'])
                < datetime.now()):
            return None
        return self.user_id_by_session_id[session_id]['user_id']
