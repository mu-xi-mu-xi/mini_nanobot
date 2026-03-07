from typing import List
from memory.base import BaseMemory
from core.message import Message

class MemoryStore(BaseMemory):

    def __init__(self, max_size: int = 100):
        self.records: List[Message] = []
        self.max_size = max_size

    def save(self, message:Message):
        self.records.append(message)
        # 控制 memory 大小
        if len(self.records) > self.max_size:
            self.records.pop(0)

    def retrieve(self, query:Message):
        results = []
        for r in reversed(self.records):
            if query.content in r.content:
                results.append(Message(role="user",content=r.content))
            if len(results) >= 3:
                break
        if not results:
            return None
        return results