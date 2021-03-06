#!/usr/bin/env python3
""" Basic auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Inherits from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """ Returns the Base64 part of the Authorization header for a
            Basic Authentication
        """
        if authorization_header is None or\
           type(authorization_header) is not str:
            return None
        hd = authorization_header.split(' ')
        return hd[1] if hd[0] == 'Basic' else None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Returns the decoded value of a Base64 string base64_auth_header
        """
        if base64_authorization_header is None or\
           type(base64_authorization_header) is not str:
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('utf-8')
            return message
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Returns the user email and password from the Base64 decoded value
        """
        if not decoded_base64_authorization_header or\
           not isinstance(decoded_base64_authorization_header, str)\
           or ":" not in decoded_base64_authorization_header:
            return (None, None)
        extract = decoded_base64_authorization_header.split(':', 1)
        return (extract[0], extract[1]) if extract else (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password
        """
        if not user_email or not isinstance(user_email, str)\
           or not user_pwd or not isinstance(user_pwd, str):
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Overloads Auth and retrieves the User instance for a request
        """
        try:
            header = self.authorization_header(request)
            base64_h = self.extract_base64_authorization_header(header)
            decode_h = self.decode_base64_authorization_header(base64_h)
            credents = self.extract_user_credentials(decode_h)
            return self.user_object_from_credentials(credents[0], credents[1])
        except Exception:
            return None
