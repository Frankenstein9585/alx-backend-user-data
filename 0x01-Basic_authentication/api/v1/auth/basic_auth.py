#!/usr/bin/env python3
"""This file contains the BasicAuth class"""
import base64
import binascii
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class inherits from Auth"""

    def __init__(self):
        """Init Method"""
        super().__init__()

    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """Returns the Base64 part of the Authorization header"""
        if not authorization_header:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) \
            -> str:
        """Returns the decoded value of the Base64 string"""
        if (not base64_authorization_header or
                type(base64_authorization_header) != str):
            return None
        try:
            return (base64.b64decode(base64_authorization_header).
                    decode('utf-8'))
        except binascii.Error:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Returns the user email and password from the Base64 decoded value"""
        if (not decoded_base64_authorization_header or
                type(decoded_base64_authorization_header) != str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        uname = decoded_base64_authorization_header.split(':')[0]
        pwd = decoded_base64_authorization_header.split(':')[1]

        return uname, pwd

    def user_object_from_credentials(self, user_email: str, user_pwd: str) \
            -> TypeVar('User'):
        """Returns the User based on his email and Password"""
        if not user_email or type(user_email) != str:
            return None

        if not user_pwd or type(user_pwd) != str:
            return None

        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None
