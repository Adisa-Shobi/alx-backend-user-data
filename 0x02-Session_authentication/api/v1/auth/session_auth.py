#!/usr/bin/python3
'''
Definition of SessionAuth inherits from Auth
'''
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    '''
    Implemetation of SessionAuth creates authentication sessions
    '''

    # def create_session(self, user_id: str = None) -> str:
    #    '''
    #    Initializes by creating a session
    #    '''
