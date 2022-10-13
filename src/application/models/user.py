from src.application.models.account import Account
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: Optional[str]
    username: str
    account: Optional[Account]
    account_id: int
    
    class Config:
        orm_mode=True
