#!/usr/bin/env python3
'''
Defines utility for authentication
'''
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid
from typing import Union


def _hash_password(password: str) -> bytes:
    '''Hashes passwords
    '''
    hashed_pw = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
    return hashed_pw


def _generate_uuid() -> str:
    '''Generates an id
    '''
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''Registers a new user object
        '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            self._db.add_user(email, hashed_password)
        else:
            raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        '''methods validates login
        '''
        try:
            user = self._db.find_user_by(email=email)
        except (InvalidRequestError, NoResultFound):
            return False
        return bcrypt.checkpw(bytes(password, 'utf-8'), user.hashed_password)

    def create_session(self, email: str) -> Union[str, None]:
        '''Creates a session for new user
        '''
        try:
            user = self._db.find_user_by(email=email)
        except (InvalidRequestError, NoResultFound):
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(session_id: str) -> Union[str, None]:
        '''
        Retrieves user by session_id
        '''
        # if session_id is None:
        #    return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except (InvalidRequestError, NoResultFound):
            return None
        return user
