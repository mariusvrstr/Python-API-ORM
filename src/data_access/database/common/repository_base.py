from abc import ABC
from sqlalchemy.orm import Session

class RepositoryBase(ABC):
    context = None

    def __init__(self, context: Session) -> None:
        self.context = context

    def sync(self):
        self.context.flush()
