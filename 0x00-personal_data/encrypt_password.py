#!/usr/bin/env python3
"""Encrypt Password Module"""
from typing import ByteString

import bcrypt


def hash_password(password: str) -> ByteString:
    """This function hashes a password using bcrypt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
