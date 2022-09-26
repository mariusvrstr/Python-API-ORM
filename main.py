from src.data_access.models import user_entity
from src.data_access.models import account_entity
from src.data_access.common.database import engine


# Create database
user_entity.Base.metadata.create_all(engine)