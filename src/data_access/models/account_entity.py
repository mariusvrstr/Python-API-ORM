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

class account_entity(Base):
    __tablename__ = 'Accounts'

    #id = Column('Id', UUID(),primary_key=True,default=uuid.uuid4)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(String)

    # Foreign Key - Many Side Opposed to One
    users = relationship('user_entity', back_populates='')