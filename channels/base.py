from abc import ABC,abstractmethod
from core.message import Message

class Channel(ABC):
    @abstractmethod
    def send(self,message:Message):
        pass
    @abstractmethod
    def receive(self)->Message:
        pass