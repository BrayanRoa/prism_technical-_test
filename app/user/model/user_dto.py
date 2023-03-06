from werkzeug.security import generate_password_hash


class UserDTO():
    
    def __init__(self, usernama, email, passw) -> None:
        self.username = usernama
        self.email = email
        self.passw = generate_password_hash(passw)
    