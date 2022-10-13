from src.application.models.account import Account

class AccountBuilder(Account):

    def __init__(self) -> None:
        super().__init__(id=0, name='', account_number='')

    def inoxico(self):
        self.id = 1
        self.name = 'Inoxico'
        self.account_number = '001'
        return self        

    def build(self) -> Account:
        account = Account(id=self.id, name=self.name, account_number=self.account_number)
        return account
