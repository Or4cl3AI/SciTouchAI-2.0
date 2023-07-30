```python
import hashlib
import binascii
import os

def authenticateUser(username, password, db_password_hash, db_salt):
    """
    This function authenticates the user by comparing the password hash stored in the database
    with the hash of the password entered by the user.
    """
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), db_salt, 100000)
    return binascii.hexlify(password_hash) == db_password_hash

def hash_password(password):
    """
    This function generates a new salt and a hash of the password for storing in the database.
    """
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return binascii.hexlify(password_hash), salt
```