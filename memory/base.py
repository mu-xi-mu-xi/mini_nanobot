from abc import ABC, abstractmethod
from core.message import Message

class BaseMemory(ABC):

    def __init__(self):
        self.memory=[]
    @abstractmethod
    def save(self, message:Message):
        """
        保存记忆
        """
        pass

    @abstractmethod
    def retrieve(self, query:Message):
        """
        根据query检索相关记忆
        """
        pass