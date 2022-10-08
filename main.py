from test.builders.account_builder import AccountBuilder
from test.builders.user_builder import UserBuilder
from src.application.models.user import User
from src.application.models.requests.new_user_request import NewUserRequest
from src.application.services.admin_service import AdminService
from src.data_access.database.models import database_models
from src.data_access.database.common.database import get_db_Session, engine

context = get_db_Session()
admin_service = AdminService(context)

# Build sample objects
sample_account = AccountBuilder().inoxico().build()
sample_user = UserBuilder().super_user().build()

def remove(user: User):
    admin_service.delete_user(user.id)
    admin_service.delete_account(user.account_id)

def populate():
    new_account = admin_service.add_account(sample_account)
    new_user_req = NewUserRequest(sample_user.name, sample_user.username, 'Password123', new_account.id if new_account is not None else None)
    admin_service.add_user(new_user_req)

def main():    
    # Unit of work pattern
    try:
        database_models.Base.metadata.create_all(engine) # Create/Sync database

        found_sample_user = admin_service.get_user(sample_user.username)
        print(found_sample_user)
        
        is_populated = (found_sample_user is not None)
        if is_populated:
            remove(found_sample_user)
        
        populate()            

        context.commit() # Persist changes if all was successfull

    except Exception as ex:
        print(f"Oops! {ex.__class__} occurred. Details: {ex}")  
    finally:
        context.close() # Always close the database connection

main()






