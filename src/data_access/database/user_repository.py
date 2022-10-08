from src.application.models.user import User
from src.data_access.database.models.database_models import AccountEntity, UserEntity
from src.data_access.database.common.repository_base import RepositoryBase

class UserRepository(RepositoryBase):   

    def map_to_business(self, user: UserEntity) -> User:
        if (user == None):
            return None

        mapped = User(user.name, user.username, user.account_id)
        return mapped

    def map_to_database(self, user: User) -> UserEntity:
        raise ValueError(f'Unable to add map user directly, password hash needs to be calculated first. Username [{user.username}]') 

    def __init__(self, context) -> None:
        super().__init__(context, UserEntity, User)

    # Special override because password is handled seperate to general user data
    def add_user_with_password(self, user: User, password_hash):        
        new_user = UserEntity().create(user.name, user.username, password_hash, user.account_id)
        self.context.add(new_user)
        self.sync()

        return user

    def get_user(self, username) -> User:
        user = self.context.query(UserEntity).filter(UserEntity.username == username).first() #TODO: Must be an select single
        return user