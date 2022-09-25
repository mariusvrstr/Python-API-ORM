from abc import ABC

class RepositoryBase(ABC):
    context = None

    def __init__(self, context) -> None:
        self.context = context

    def save(self):
        self.save()
