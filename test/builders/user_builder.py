from src.application.models.user import User

class UserBuilder(User):

    def __init__(self) -> None:
        super().__init__(id=0,name='',username='',account_id=0)

    def super_user(self):
        self.id = 1
        self.name = 'Super User'
        self.username = 'root'
        return self        

    def build(self) -> User:
        user = User(id=self.id, name=self.name, username=self.username, account=self.account, account_id=self.account_id)
        return user
