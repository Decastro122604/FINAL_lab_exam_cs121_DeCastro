# user.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.points = 0
        self.wins = 0

    def __repr__(self):
        return f"User('{self.username}')"
