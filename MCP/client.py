import requests


class MCPClient:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def list_tools(self):
        resp = requests.get(f"{self.base_url}/tools")
        resp.raise_for_status()
        return resp.json()

    def run_tool(self, name: str, arguments: dict):

        resp = requests.post(
            f"{self.base_url}/run",
            json={
                "tool": name,
                "arguments": arguments
            }
        )

        resp.raise_for_status()
        return resp.json()