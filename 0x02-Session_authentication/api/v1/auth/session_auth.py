#!/usr/bin/python3
'''
Definition of SessionAuth inherits from Auth
'''
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    '''
    Implemetation of SessionAuth creates authentication sessions
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        Initializes by creating a session
        '''
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id