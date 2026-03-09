from core.message import Message
from memory.base import BaseMemory
class ShortMemory(BaseMemory):

    def __init__(self, max_turns=20):
        self.messages:list[Message] = []
        self.max_turns = max_turns

    def add(self,message:Message):
        self.messages.append(message)
        if len(self.messages) > self.max_turns:
            self.messages.pop(0)

    def get(self):
        return self.messages

    def clear(self):
        self.messages = []
    
