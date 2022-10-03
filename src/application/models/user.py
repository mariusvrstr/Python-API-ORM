from src.application.models.account import Account

class User():
    id = None
    name = None
    username = None
    account = None

    def __init__(self, name, username, account: Account) -> None:
        self.name = name
        self.username = username
        self.account = account
