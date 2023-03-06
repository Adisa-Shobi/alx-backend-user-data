#!/usr/bin/env python3
'''
class to manage the API authentication.
'''
from flask import request


class Auth:
    '''
    Manages authentication for api
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        auth mthd
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''
        To be implemented
        '''
        return False

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        To be implemented
        '''
        return None
