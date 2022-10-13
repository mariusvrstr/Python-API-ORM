from src.application.models.account import Account
from src.application.models.user import User
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

    def add_account(self, account: Account):
        return self.account_repo.add_account(account)

    def get_account(self, account_number):
        return self.account_repo.get_account(account_number)

    def add_user(self, new_user_req: NewUserRequest):
        user = User(id=-1, name=new_user_req.name, username=new_user_req.username, account_id=new_user_req.account_id)

        # Hash Password
        hash_object = hashlib.sha256(new_user_req.password.encode('utf-8'))
        hash_password = hash_object.hexdigest()

        return self.user_repo.add_user_with_password(user, hash_password)        

    def get_user(self, username):
        return self.user_repo.get_user(username)

    def delete_user(self, id):
        return self.user_repo.delete(id)

    def delete_account(self, id):
        return self.account_repo.delete(id)