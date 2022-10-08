from src.application.models.account import Account

class User():
    id = None
    name = None
    username = None
    account = None
    account_id = None

    def __init__(self, name, username, account_id, account: Account = None) -> None:
        self.name = name
        self.username = username
        self.account_id = account_id
        self.account = account
