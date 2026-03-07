from tools.base import Tool


class MCPTool(Tool):

    def __init__(self, name, description, parameters, client):
        super().__init__(name, description, parameters)
        self.client = client

    def run(self, arguments):

        return self.client.run_tool(
            name=self.name,
            arguments=arguments
        )