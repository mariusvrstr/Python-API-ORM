from src.application.models.account import Account
from src.data_access.common.repository_base import RepositoryBase

class AccountRepository(RepositoryBase):

    def __init__(self, context) -> None:
        super().__init__(context)

    def add_account(self, name, account_number):
        # Check that account does not exist
        pass

    def get_account(self, username) -> Account:
        pass