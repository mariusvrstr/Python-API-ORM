from src.application.models.account import Account

class User():
    id = None
    name = None
    username = None
    email = None
    account = None

    def __init__(self, name, username, email, account) -> None:
        self.name = name
        self.username = username
        self.email = email
        self.account = account
