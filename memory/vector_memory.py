from memory.base import BaseMemory
class VectorMemory(BaseMemory):

    def __init__(self):

        self.data = []
        self.top_k=3

    def add(self, text):

        self.data.append(text)

    def get(self):

        # mini版先简单 keyword
        results = []

#        for t in self.data:
#            if query in t:
#                results.append(t)

        return results[:self.top_k]
    
    def clear(self):
        pass