from src.data_access.database.models.database_models import AccountEntity
from src.application.models.account import Account
from src.data_access.database.common.repository_base import RepositoryBase
from sqlalchemy.sql import select

class AccountRepository(RepositoryBase):

    def __init__(self, context ) -> None:
        super().__init__(context)

    def add_account(self, name, account_number):
        new_account = AccountEntity().create(name, account_number)
        account = self.context.add(new_account)
        return account

    def get_account_by_id(self, id):
        account = self.context.get(AccountEntity, id)
        return account

    def get_account(self, account_number) -> Account:
        accounts = self.context.query(AccountEntity).all() #TODO: Must be an select single # filter(account_number = account_number)

        if (len(accounts) == 0):
            return None

        account = accounts.pop()        
        mapped_account = Account(account.name, account.account_number)
        mapped_account.id = account.id

        return mapped_account