#!/usr/bin/env python3
'''
class BasicAuth that inherits from Auth
'''
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    '''
    BasicAuth, a variation of Auth
    '''

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''
        returns the Base64 part of the Authorization
        header for a Basic Authentication
        '''
        if authorization_header and isinstance(authorization_header, str):
            syntax_a = authorization_header.startswith("Basic ")
            if not syntax_a:
                return None
            auth_data = authorization_header.split(" ")[-1]
            return auth_data
            # decoded_data = base64.b64decode(auth_data)
            # return auth_data
        else:
            return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''
        returns the decoded value of a Base64
        string base64_authorization_header
        '''
        if base64_authorization_header and isinstance(
                base64_authorization_header, str):
            try:
                decoded_data = base64.b64decode(base64_authorization_header)
                return decoded_data.decode('utf-8')
            except Exception:
                return None
        else:
            return None
