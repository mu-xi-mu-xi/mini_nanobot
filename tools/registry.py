from tools.base import Tool
class ToolRegistry:
    def __init__(self):
        self.tools={}
    
    def register(self,tool:Tool):
        self.tools[tool.name]=tool

    def get(self,name:str)->Tool|None:
        return self.tools.get(name)
    
    def list_tools(self)->list[Tool]:
        return list(self.tools.values())
    
    def schemas(self):
        return [tool.schema() for tool in self.tools.values()]