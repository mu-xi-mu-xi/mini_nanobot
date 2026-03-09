from abc import ABC, abstractmethod
from core.message import Message

class BaseMemory(ABC):

    def __init__(self):
        self.memory=[]
    @abstractmethod
    def add(self, message:Message):
        """
        保存记忆
        """
        pass

    @abstractmethod
    def get(self):
        """
        根据query检索相关记忆
        """
        pass

    @abstractmethod
    def clear(self):
        """
        清理memory
        """
        pass
