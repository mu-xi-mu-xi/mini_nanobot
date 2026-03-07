from channels.base import Channel
from core.message import Message

class CLIChannel(Channel):
    def __init__(self):
        pass
    def send(self,message:str):
        print(f"Assistant: {message}")

    def receive(self)->Message:
        text=input("You can ask me anything:")
        return Message(role="user",content=text)