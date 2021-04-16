#!/usr/bin/env python3
""" Auth module
"""
import bcrypt
from db import DB


def _hash_password(password: str) -> str:
    """ Takes in a password string arguments and returns bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        """ Initailize
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Take mandatory email and password string arguments and return
            a User object
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists.".format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
