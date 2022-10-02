from ast import Index
import email
from tokenize import String
from unicodedata import name
from src.data_access.database.common.database import Base
# from src.data_access.common.database import UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column
import uuid

class AccountEntity(Base):
    __tablename__ = 'Accounts'

    #id = Column('Id', UUID(),primary_key=True,default=uuid.uuid4)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    account_number = Column(String)

    # Foreign Key - Many Side Opposed to One
    users = relationship('UserEntity', back_populates='')

    def create(self, name, account_number):
        self.name = name
        self.account_number = account_number

        return self

class UserEntity(Base):
    __tablename__ = 'Users'

    #id = Column('Id', UUID(),primary_key=True,default=uuid.uuid4)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String)
    password_hash = Column(String)

    # Foreign Key - One Side Oposed to Many
    account_id = Column(Integer, ForeignKey('Accounts.id'))

    def create(self, name, username, password_hash, account_id):
        self.name = name
        self.username = username
        self.password_hash = password_hash
        self.account_id = account_id

        return self