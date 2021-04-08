#!/usr/bin/env python3
""" Expiration date to a Session ID
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """ Inherits from SessionAuth
    """
    def __init__(self):
        """ Initialization
        """
        s_duration = getenv('SESSION_DURATION')
        if s_duration:
            self.session_duration = int(s_duration)
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Create a Session ID
        """
        if not user_id:
            return
        session_id = super().create_session(user_id)
        if not session_id:
            return
        user_id = self.user_id_by_session_id.get(session_id)
        if not user_id:
            return
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Return user_id from the session dictionary
        """
        if not session_id:
            return
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if not session_dictionary:
            return
        user_id = session_dictionary.get('user_id')
        if not user_id:
            return
        if self.session_duration <= 0:
            return user_id
        created_at = session_dictionary.get('created_at')
        if not created_at:
            return
        if datetime.now() > created_at + timedelta(seconds=self
                                                   .session_duration):
            return
        return user_id
