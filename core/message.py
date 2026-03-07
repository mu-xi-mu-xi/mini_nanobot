class Message:
    def __init__(
            self,
            role:str,
            content:str="",
            name:str|None=None
    ):
        self.role=role
        self.content=content
        self.name=name

class Session:
    def __init__(self):
        self.messages:list[Message]=[]
    def add(self,message:Message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages