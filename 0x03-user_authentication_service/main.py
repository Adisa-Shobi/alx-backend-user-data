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

app.app.run()
print(auth.get_reset_password_token(email))
print(auth.get_reset_password_token("unknown@email.com"))
