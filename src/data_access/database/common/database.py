from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import types
from sqlalchemy.dialects.mysql.base import MSBinary
import uuid

## SQL Server
## SQLALCHEMY_DATABASE_URL = "mssql://*localhost*/*test_db*?trusted_connection=yes'"
## SQL Lite
SQLALCHEMY_DATABASE_URL = "sqlite:///./sample_app.db"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()

##TODO: Get GUID ID's to work
'''
class UUID(types.TypeDecorator):
    impl = MSBinary
    def __init__(self):
        self.impl.length = 16
        types.TypeDecorator.__init__(self,length=self.impl.length)

    def process_bind_param(self,value,dialect=None):
        if value and isinstance(value,uuid.UUID):
            return value.bytes
        elif value and not isinstance(value,uuid.UUID):
            raise ValueError,'value %s is not a valid uuid.UUID' % value
        else:
            return None

    def process_result_value(self,value,dialect=None):
        if value:
            return uuid.UUID(bytes=value)
        else:
            return None

    def is_mutable(self):
        return False
'''

def get_db():
    db = session_local()

    try:
        yield db
    finally:
        db.close()