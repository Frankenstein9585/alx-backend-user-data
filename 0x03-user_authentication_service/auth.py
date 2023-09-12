#!/usr/bin/env python3
"""auth.py for Authentication"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt"""
    return hashpw(password.encode(), gensalt())
