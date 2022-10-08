from src.data_access.database.models.database_models import AccountEntity
from src.application.models.account import Account
from src.data_access.database.common.repository_base import RepositoryBase
from sqlalchemy.sql import select

class AccountRepository(RepositoryBase):

    def map(self, account: AccountEntity) -> Account:
        if (account == None):
            return None

        mapped = Account(account.name, account.account_number)
        mapped.id = account.id
        return mapped

    def __init__(self, context ) -> None:
        super().__init__(context)

    def add_account(self, name, account_number):
        new_account = AccountEntity().create(name, account_number)
        self.context.add(new_account)
        self.sync()
        account = self.get_account(account_number)
        
        return self.map(account)

    def get_account_by_id(self, id):
        account = self.context.get(AccountEntity, id)
        return self.map(account)

    def get_account(self, account_number) -> Account:
        account = self.context.query(AccountEntity).filter(AccountEntity.account_number == account_number).first() #TODO: Must be an select single # filter(account_number = account_number)

        return self.map(account)