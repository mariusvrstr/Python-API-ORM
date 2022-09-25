from src.data_access.common.repository_base import RepositoryBase

class UserRepository(RepositoryBase):

    def __init__(self, context) -> None:
        super().__init__(context)

    def add_user(user, role):
        #TODO: Convert from business to DAL model and persist
        pass