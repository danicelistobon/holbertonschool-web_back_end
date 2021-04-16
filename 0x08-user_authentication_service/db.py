#!/usr/bin/env python3
""" DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """ DB class
    """
    def __init__(self):
        """ Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Has two required string arguments: email and hashed_password, and
            returns a User object, the method should save the user to the db
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ Takes in arbitrary keyword arguments and returns the first row
            found in the users table as filtered by the methods input args
        """
        user_keys = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token']

        for key in kwargs.keys():
            if key not in user_keys:
                raise InvalidRequestError
        result = self._session.query(User).filter_by(**kwargs).first()
        if result is None:
            raise NoResultFound
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """ That takes as argument a required user_id integer and arbitrary
            keyword arguments, and returns None
        """
        user_to_update = self.find_user_by(id=user_id)

        user_keys = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token']

        for key, value in kwargs.items():
            if key in user_keys:
                setattr(user_to_update, key, value)
            else:
                raise ValueError
        self._session.commit()
