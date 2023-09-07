#!/usr/bin/env python3
"""This file contains the SessionAuth Class"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """The SessionAuth Class"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
