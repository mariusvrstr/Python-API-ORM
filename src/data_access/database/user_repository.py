from src.application.models.user import User
from src.data_access.database.common.repository_base import RepositoryBase

class UserRepository(RepositoryBase):

    def __init__(self, context) -> None:
        super().__init__(context)

    def add_user(self, name, username, password, account_number):
        # Get account

        # Check that username is not yet taken

        # Add user

        pass

    def get_user(self, username) -> User:
        pass