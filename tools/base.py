from abc import ABC,abstractmethod
from typing import Callable
class Tool(ABC):
    def __init__(
            self,
            name:str,
            description:str,
            parameters:dict
    ):
        self.name=name
        self.description=description
        self.parameters=parameters
    
    def schema(self):
        return {
            "type":"function",
            "function":{
                "name":self.name,
                "description":self.description,
                "parameters":self.parameters
            }

        }
    
    @abstractmethod
    def run(self, arguments: dict):
        pass