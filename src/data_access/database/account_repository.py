from src.data_access.database.models.database_models import AccountEntity
from src.application.models.account import Account
from src.data_access.database.common.repository_base import RepositoryBase
from sqlalchemy.sql import select

class AccountRepository(RepositoryBase):

    def map_to_business(self, account: AccountEntity) -> Account:
        if (account == None):
            return None

        mapped = Account(account.name, account.account_number, account.id)
        return mapped

    def map_to_database(self, account: Account) -> AccountEntity:
        if (account == None):
            return None
        
        mapped = AccountEntity().create(account.name, account.account_number)
        return mapped


    def __init__(self, context) -> None:
        super().__init__(context, AccountEntity, Account)

    def get_account(self, account_number) -> Account:
        account = self.context.query(AccountEntity).filter(AccountEntity.account_number == account_number).first() #TODO: Must be an select single # filter(account_number = account_number)

        return self.map(account)