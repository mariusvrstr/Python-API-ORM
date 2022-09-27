from src.application.models.account import Account

class AccountBuilder(Account):

    def __init__(self) -> None:
        super().__init__('', '')

    def inoxico(self):
        self.id = 1
        self.name = 'Inoxico'
        self.account_number = '001'
        return self        

    def build(self) -> Account:
        account = self
        account.__class__ = Account
        return account
