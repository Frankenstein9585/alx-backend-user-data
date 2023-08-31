#!/usr/bin/env python3
"""Filtered Logger Module"""
import re

from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates a log msg using re.sub()"""
    for field in fields:
        if field in message:
            message = re.sub(r"{}=.*?{}".format(field, separator),
                             '{}={}{}'.format(field, redaction, separator),
                             message)
    return message
