#!/usr/bin/env python3
""" Model UserSession
"""
from models.base import Base


class UserSession(Base):
    """ Inherits from Base
    """
    def __init__(self, *args: list, **kwargs: dict):
        """ Initialization
        """
        super().__init__(*args, **kwargs)
        self.user_id: str = kwargs.get('user_id')
        self.session_id: str = kwargs.get('session_id')
