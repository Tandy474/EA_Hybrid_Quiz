#  user authentication by checking users.csv
import csv

class LoginManager:
    def __init__(self, csv_path="users.csv"):
        self.csv_path = csv_path                     # Path to users CSV
        self.users = self.load_users()               # Load all users

    def load_users(self):
        users = {}                                   #  username → password
        with open(self.csv_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                users[row["username"]] = row["password"]
        return users

    def authenticate(self, username, password):
        return username in self.users and self.users[username] == password
