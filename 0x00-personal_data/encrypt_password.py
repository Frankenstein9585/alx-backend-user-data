#!/usr/bin/env python3
"""Encrypt Password Module"""
from typing import ByteString

import bcrypt


def hash_password(password: str) -> bytes:
    """This function hashes a password using bcrypt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates the password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
