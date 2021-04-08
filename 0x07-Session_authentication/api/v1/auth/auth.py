#!/usr/bin/env python3
""" Auth class
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method that returns False - path and excluded_paths
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p.endswith('*'):
                if path.startswith(p[:1]):
                    return False
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ Public method that returns None - request will be the Flask
            request object
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method hat returns None - request will be the Flask
            request object
        """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request
        """
        if not request:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
