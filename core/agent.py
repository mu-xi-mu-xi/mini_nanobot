from core.message import Message, Session
from core.response import LLMResponse
from providers.base import Provider
from tools.registry import ToolRegistry
from memory.base import BaseMemory
from core.prompt_loader import PromptLoader
class Agent:
    def __init__(
            self,
            provider:Provider,
            tool_registry:ToolRegistry,
            max_iterations:int=5,
            history:Session|None=None,
            memory:BaseMemory|None=None,
            system_message:Message|None=None
        ):
        self.history=history or Session()
        self.provider=provider
        self.tool_registry=tool_registry
        self.max_iterations=max_iterations
        self.memory=memory
        self.system_message=Message(role="system",content=PromptLoader().load("system"))

    def  build_message(self,message:Message):
        self.history.add(message)
        if self.memory:
            self.memory.save(message)
        memory_message=[]
        if self.memory:
            memory_messages=self.memory.retrieve(self.history.get_messages()[-1]) 
        else:
            memory_messages=self.history.get_messages()
        if memory_message:
                messages=[self.system_message]+memory_messages+self.history.get_messages()
            
        else:
            messages=[self.system_message]+self.history.get_messages()
            
        return messages

    def run(self,initial_message:Message):
        messages=self.build_message(initial_message)
        for i in range(self.max_iterations):
            res:LLMResponse=self.provider.chat(messages=messages,tools=self.tool_registry.schemas())
            message=Message(role="assistant",content=res.content)
            messages=self.build_message(message)
            if res.has_tool_calls():
                for tool_call in res.tool_calls:
                    tool=self.tool_registry.get(tool_call.name)
                    if not tool:
                        raise Exception(f"Tool {tool_call.name} not found")
                    else:
                        args = tool_call.arguments

                        if isinstance(args, str):
                            import json
                            args = json.loads(args)

                        tool_call_res = tool.run(args)
                        self.history.add(Message(role="tool",content=str(tool_call_res),name=tool_call.name))
                continue
            return res.content
        raise Exception("Max iterations reached")
