from abc import ABC, abstractmethod

class BaseReport(ABC):
    @abstractmethod
    def generate(self, data:dict) -> dict:
        pass