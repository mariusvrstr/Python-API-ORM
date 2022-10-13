from src.application.models.user import User
from src.data_access.database.models.database_models import AccountEntity, UserEntity
from src.data_access.database.common.repository_base import RepositoryBase

class UserRepository(RepositoryBase):   

    def __init__(self, context) -> None:
        super().__init__(context, UserEntity, User)

    # Special override because password is handled seperate to general user data
    def add_user_with_password(self, user: User, password_hash):        
        new_user = UserEntity().create(user.name, user.username, password_hash, user.account_id)
        self.context.add(new_user)
        self.sync()
        return self.map(new_user)

    def get_user(self, username) -> User:
        user = self.context.query(UserEntity).filter(UserEntity.username == username).first() #TODO: Must be an select single
        return self.map(user)