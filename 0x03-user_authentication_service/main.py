#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth
app = __import__("app")

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

reset_token = auth.get_reset_password_token(email)

print(auth.valid_login(email, password))
new_password = "password"
auth.update_password(reset_token, new_password)
print(auth.valid_login(email, password))
print(auth.valid_login(email, new_password))
