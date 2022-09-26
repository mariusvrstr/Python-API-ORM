from ast import Index
import email
from tokenize import String
from unicodedata import name
from src.data_access.common.database import Base
# from src.data_access.common.database import UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column
import uuid

class user_entity(Base):
    __tablename__ = 'Users'

    #id = Column('Id', UUID(),primary_key=True,default=uuid.uuid4)
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    # Foreign Key - One Side Oposed to Many
    account_id = Column(Integer, ForeignKey('Accounts.id'))
    account = relationship('account_entity', back_populates='Users')



