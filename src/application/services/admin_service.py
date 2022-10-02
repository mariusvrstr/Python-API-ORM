from src.data_access.database.account_repository import AccountRepository
from src.data_access.database.user_repository import UserRepository
from src.application.models.requests.new_user_request import NewUserRequest
from sqlalchemy.orm import Session

import hashlib

class AdminService():
    context = None
    account_repo = None
    user_repo = None

    def __init__(self, context) -> None:
        self.context = context
        self.account_repo = AccountRepository(context)
        self.user_repo = UserRepository(context)

    def add_account(self, account_name, account_number):
        account = self.account_repo.add_account(account_name, account_number)
        return account

    def get_account(self, account_number):
        account = self.account_repo.get_account(account_number)
        return account

    def add_user(self, new_user_req: NewUserRequest):

        # Hash Password
        hash_object = hashlib.sha256(new_user_req.password.encode('utf-8'))
        hash_password = hash_object.hexdigest()

        # Session.refresh(self.context)

        account = self.account_repo.get_account(new_user_req.account_number)

        if (account == None):
            raise ValueError(f'Unable to add user [{new_user_req.name}] to account [{new_user_req.account_number}] as the account does not exist.')

        user = self.user_repo.add_user(new_user_req.name, new_user_req.username, hash_password, account.id)
        return user

    def get_user(self, username):
        user = self.user_repo.get_user(username)
        return user