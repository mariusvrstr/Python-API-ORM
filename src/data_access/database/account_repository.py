from src.data_access.database.models.database_models import AccountEntity
from src.application.models.account import Account
from src.data_access.database.common.repository_base import RepositoryBase
from sqlalchemy.sql import select

class AccountRepository(RepositoryBase):

    def __init__(self, context) -> None:
        super().__init__(context, AccountEntity, Account)

    def add_account(self, acccount: Account) -> Account:
        db_account = AccountEntity().create(acccount.name, acccount.account_number)
        return self.add(db_account)


    def get_account(self, account_number) -> Account:
        account = self.context.query(AccountEntity).filter(AccountEntity.account_number == account_number).first() #TODO: Must be an select single # filter(account_number = account_number)

        return self.map(account)