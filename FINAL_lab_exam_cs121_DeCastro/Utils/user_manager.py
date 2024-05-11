# user_manager.py

from Utils.user import User

class UserManager:
    def __init__(self):
        self.users = []
        self.load_users()

    def load_users(self):
        try:
            with open("users.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    username, password, points, wins = line.strip().split(",")
                    self.users.append(User(username, password, int(points), int(wins)))
        except FileNotFoundError:
            # If users file doesn't exist, initialize with an empty list
            self.users = []

    def save_users(self):
        with open("users.txt", "w") as file:
            for user in self.users:
                file.write(f"{user.username},{user.password},{user.points},{user.wins}\n")

    def validate_username(self, username):
        if len(username) < 4:
            print("Username must be at least 4 characters long.")
            return False
        for user in self.users:
            if user.username == username:
                print("Username already exists. Please choose a different one.")
                return False
        return True

    def validate_password(self, password):
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return False
        return True

    def register(self):
        print("Register a new user:")
        username = input("Enter username: ")
        if not self.validate_username(username):
            return
        password = input("Enter password: ")
        if not self.validate_password(password):
            return
        self.users.append(User(username, password))
        self.save_users()
        print("Registration successful.")

    def login(self):
        print("Login:")
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.username == username and user.password == password:
                print("Login successful.")
                return user
        print("Invalid username or password.")
        return None