# main.py
from core.agent import Agent
from core.message import Message, Session
from providers.zhipu import ZhipuProvider
from tools.registry import ToolRegistry
from tools.builtin.weather import WeatherTool
from channels.cil import CLIChannel
from skills.loader import SkillLoader
from memory.store import MemoryStore
from MCP.manager import MCPManager
channel=CLIChannel()
# 创建 ToolRegistry
memory=MemoryStore()



tool_registry = ToolRegistry()

mcp_manager=MCPManager(tool_registry)
mcp_manager.connect(base_url="http://localhost:8000")

skill_loader = SkillLoader(tool_registry)
skill_loader.load_skill()
# 注册工具
weather_tool = WeatherTool()
tool_registry.register(weather_tool)

# 创建 Provider
provider = ZhipuProvider()

# 创建 Agent
agent = Agent(provider=provider, tool_registry=tool_registry, memory=memory)
while True:
    user_message = channel.receive()
    response = agent.run(user_message)
    channel.send(response)
    