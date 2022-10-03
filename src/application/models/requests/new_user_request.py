

class NewUserRequest():
    name = None
    username = None
    password = None
    account_id = None

    def __init__(self, name, username, password, account_id) -> None:
        self.name = name
        self.username = username
        self.password = password
        self.account_id = account_id