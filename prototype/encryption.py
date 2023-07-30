```python
from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_data(data):
    """
    Encrypts data
    """
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    return encrypted_data
```