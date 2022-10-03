from src.application.models.user import User

class UserBuilder(User):

    def __init__(self) -> None:
        super().__init__('','','')

    def super_user(self):
        self.id = 1
        self.name = 'Super User'
        self.username = 'root'
        return self        

    def build(self) -> User:
        account = self
        account.__class__ = User
        return account
