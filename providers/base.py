from abc import ABC,abstractmethod
from core.message import Message
from core.response import LLMResponse

class Provider(ABC):
    @abstractmethod
    def chat(self,messages:list[Message])->LLMResponse:
        pass