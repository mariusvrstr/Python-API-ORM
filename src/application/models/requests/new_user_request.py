

class NewUserRequest():
    name = None
    username = None
    password = None
    email = None
    account_number = None

    def __init__(self, name, username, password, email, account_number) -> None:
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.account_number = account_number