import os
from dotenv import load_dotenv
from zhipuai import ZhipuAI
from providers.base import Provider
from core.response import LLMResponse, ToolCall
from core.message import Message
from tools.base import Tool

load_dotenv()
class ZhipuProvider(Provider):
    def __init__(self,model:str="GLM-4.7-Flash"):
        self.api_key = os.getenv("ZHIPU_API_KEY")
        if not self.api_key:
            raise ValueError("ZHIPU_API_KEY environment variable not set")
        self.client=ZhipuAI(api_key=self.api_key)
        self.model=model
    
    def  _convert_messages(self, messages: list[Message]):
        result=[]
        for message in messages:
            result.append({
                "role":message.role,
                "content":message.content,
                "name":message.name or None 
            })
        return result
    def chat(self,messages:list[Message],tools:list)->LLMResponse:
        api_messages=self._convert_messages(messages)
        resp=self.client.chat.completions.create(
            model=self.model,
            messages=api_messages,
            tools=tools
        )
        choice=resp.choices[0].message
        content=choice.content
        tool_calls=[]
        if choice.tool_calls:
            
            for tc in choice.tool_calls:
                tool_calls.append(
                    ToolCall(
                        name=tc.function.name,
                        arguments=tc.function.arguments
                    )
                )
        return LLMResponse(
            role="assistant",
            content=content,
            tool_calls=tool_calls
        )

        