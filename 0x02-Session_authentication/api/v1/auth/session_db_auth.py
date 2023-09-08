#!/usr/bin/env python3
"""This file contains the SessionDBAuth class"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """The SessionDBAuth Class"""
    def create_session(self, user_id=None):
        """Creates and stores a new instance of UserSession
        and return session"""
        user_session = UserSession()
        user_session.user_id = user_id
        user_session.save()
        return user_session.id

    def user_id_for_session_id(self, session_id=None):
        """returns the User ID by requesting UserSession
        in the database based on session_id"""
        try:
            user_session = UserSession.get(session_id)
            if user_session:
                return user_session.user_id
        except KeyError:
            return None

    def destroy_session(self, request=None):
        """destroys the UserSession based on the Session
        ID from the request cookie"""
        session_id = self.session_cookie(request)
        if session_id:
            user_session = UserSession.get(session_id)
            if user_session:
                user_session.remove()