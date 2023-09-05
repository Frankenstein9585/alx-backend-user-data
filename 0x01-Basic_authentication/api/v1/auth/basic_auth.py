#!/usr/bin/env python3
"""This file contains the BasicAuth class"""
import base64
import binascii

from api.v1.auth.auth import Auth


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
