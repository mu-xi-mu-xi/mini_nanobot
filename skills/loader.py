import yaml
from tools.base import Tool
import os
import importlib
from tools.registry import ToolRegistry
from tools.function_tool import FunctionTool
class SkillLoader:
    def __init__(self,tool_registry:ToolRegistry):
        self.tool_registry=tool_registry
    def load_skill(self):
        for file in os.listdir("skills"):
            yaml_file=f"skills/{file}/skill.yaml"
            if not os.path.exists(yaml_file):
                continue
            with open(yaml_file, "r", encoding="utf-8") as f:
                config=yaml.safe_load(f)
            module=importlib.import_module(f"skills.{file}.run")
            if not hasattr(module, "run"):
                continue
            tool=FunctionTool(
                name=config["name"],
                description=config["description"],
                parameters=config["parameters"],
                func=module.run
            )
            self.tool_registry.register(tool)
    


