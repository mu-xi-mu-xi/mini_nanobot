class ToolCall:
    def __init__(self,name:str,arguments:dict):
        self.name=name
        self.arguments=arguments

class LLMResponse:
    def __init__(
            self,
            role:str,
            content:str="",
            tool_calls:list[ToolCall]|None=None
    ):
        self.role=role
        self.content=content
        self.tool_calls=tool_calls or []

    def has_tool_calls(self):
        return len(self.tool_calls)>0