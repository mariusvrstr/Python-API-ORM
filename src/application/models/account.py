from pydantic import BaseModel
from typing import Optional

class Account(BaseModel):
    id: int
    name: Optional[str]
    account_number: str
    
    class Config:
        orm_mode=True
