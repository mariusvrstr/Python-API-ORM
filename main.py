from test.builders.account_builder import AccountBuilder
from test.builders.user_builder import UserBuilder
from src.application.models.requests.new_user_request import NewUserRequest
from sqlalchemy.orm import Session
from src.application.services.admin_service import AdminService
from src.data_access.database.models import database_models
from src.data_access.database.common.database import get_db_Session, engine

context = get_db_Session()
admin_service = AdminService(context)

# Build sample objects
sample_account = AccountBuilder().inoxico().build()
sample_user = UserBuilder().super_user().build()

def populate():
    admin_service.add_account(sample_account.name, sample_account.account_number)
    '''
    The below commit is a violation of the Unit of Work pattern, I am expecting that doing a select query
    in a shared session that any uncomitted (but added in same session) data will still return but this does not
    seem to work. It might work with RAW SQL statements but not using the ORM abstractions. Need a solution for this.
    '''
    context.commit() # Hack to bypass session limitations
    new_user_req = NewUserRequest(sample_user.name, sample_user.username, 'Password123', sample_account.account_number)
    admin_service.add_user(new_user_req)

def main():    
    # Unit of work pattern
    try:
        database_models.Base.metadata.create_all(engine) # Create/Sync database

        found_sample_user = admin_service.get_user(sample_user.username)
        print(found_sample_user)
        
        is_populated = (found_sample_user is not None)
        if not is_populated:
            populate()

        context.commit() # Persist changes if all was successfull

    except Exception as ex:
        print(f"Oops! {ex.__class__} occurred. Details: {ex}")  
        context.flush() # Discard any database changes
    finally:
        context.close() # Always close the database connection

main()






