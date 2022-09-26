from src.data_access.models import user_entity
from src.data_access.models import account_entity
from src.application.models.account import Account
from src.application.models.user import User
from src.data_access.repositories.account_repository import AccountRepository
from src.data_access.repositories.user_repository import UserRepository
from src.data_access.common.database import engine

account_repo = AccountRepository()
user_repo = UserRepository()

def init():
    # Build sample objects
    account = Account() #TODO: Add builder
    user = User() #TODO: Add builder

    existing_account = account_repo.get_account(account.account_number)
    if (existing_account == None):
        account_repo.add_account(account.name, account.account_number)

    existing_user = user_repo.get_user(user.username)
    if (existing_user == None):
        user_repo.add_user(user.name, user.username, 'password123')

def main():    
    user_entity.Base.metadata.create_all(engine) # Create database
    init()


main()






