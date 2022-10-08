from src.application.models.user import User
from src.data_access.database.models.database_models import AccountEntity, UserEntity
from src.data_access.database.common.repository_base import RepositoryBase

class UserRepository(RepositoryBase):   

    def map(self, user: UserEntity) -> User:
        if (user == None):
            return None

        mapped = User(user.name, user.name, None) #TODO: Replace the None with a mapped version of lookup value

    def __init__(self, context) -> None:
        super().__init__(context)

    def add_user(self, name, username, password_hash, account_id):        
        new_user = UserEntity().create(name, username, password_hash, account_id)
        self.context.add(new_user)
        self.sync()

        user = self.get_user(username)
        return user

    def get_user_by_id(self, id):
        user = self.context.get(UserEntity, id)
        return user

    def get_user(self, username) -> User:
        user = self.context.query(UserEntity).filter(UserEntity.username == username).first() #TODO: Must be an select single
        return user