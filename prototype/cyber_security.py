import hashlib
from prototype.encryption import encryptData
from prototype.authentication import authenticateUser

class CyberSecurity:

    def __init__(self):
        self.encrypted_data = None

    def secure_data(self, data_set):
        self.encrypted_data = encryptData(data_set)

    def verify_user(self, user_input):
        return authenticateUser(user_input)

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, hash_password: str, user_password: str) -> bool:
        return hash_password == self.hash_password(user_password)

if __name__ == "__main__":
    cs = CyberSecurity()
    cs.secure_data(data_set)
    cs.verify_user(user_input)