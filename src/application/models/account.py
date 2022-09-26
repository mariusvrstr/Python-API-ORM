

class Account():
    id = None
    name = None
    account_number = None

    def __init__(self, name, account_number) -> None:
        self.name = name
        self.account_number = account_number

    def __init__(self, id, name, account_number) -> None:
        self.id = id
        self.name = name
        self.account_number = account_number