from memory.short_memory import ShortMemory
from memory.long_memory import LongMemory
from memory.vector_memory import VectorMemory
from core.message import Message

class MemoryManager:

    def __init__(self):
        self.short = ShortMemory()
        self.long = LongMemory()
        self.vector = VectorMemory()

    def add(self, message:Message):
        self.short.add(message)
    
    def get(self):
        return self.short.get()



    def add_facts(self, input:Message):
        self.long.add(input)

    def get_facts(self):
        facts=self.long.get()
        if facts:
            return [Message(role="user",content=facts)]
        else:
            return []


    def search_memory(self, query):
        return self.vector.search(query)

    def add_semantic(self, text):
        self.vector.add(text)

    