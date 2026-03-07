from MCP.client import MCPClient
from MCP.tool import MCPTool
from tools.registry import ToolRegistry

class MCPManager:

    def __init__(self, registry:ToolRegistry):
        self.registry = registry
        self.clients = []

    def connect(self, base_url: str):

        client = MCPClient(base_url)

        self.clients.append(client)

        tools = client.list_tools()

        for tool in tools:

            mcp_tool = MCPTool(
                name=tool["name"],
                description=tool["description"],
                parameters=tool["parameters"],
                client=client
            )
            self.registry.register(mcp_tool)