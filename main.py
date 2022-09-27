from src.data_access.database.models import user_entity
from src.data_access.database.models import account_entity
from test.builders.account_builder import AccountBuilder
from test.builders.user_builder import UserBuilder
from src.data_access.database.account_repository import AccountRepository
from src.data_access.database.user_repository import UserRepository
from src.data_access.database.common.database import engine

context = {} #TODO: Need to get the ORM session here
account_repo = AccountRepository(context)
user_repo = UserRepository(context)

def init():    

    # Build sample objects
    account = AccountBuilder().inoxico().build()
    user = UserBuilder().super_user().build()

    existing_account = account_repo.get_account(account.account_number)
    if (existing_account == None):
        account_repo.add_account(account.name, account.account_number)

    existing_user = user_repo.get_user(user.username)
    if (existing_user == None):
        user_repo.add_user(user.name, user.username, 'password123', account.account_number)

def main():    
    user_entity.Base.metadata.create_all(engine) # Create database
    init()

main()






