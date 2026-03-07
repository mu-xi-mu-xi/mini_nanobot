from tools.base import Tool


class FunctionTool(Tool):

    def __init__(
        self,
        name: str,
        description: str,
        parameters: dict,
        func
    ):
        super().__init__(name, description, parameters)
        self.func = func

    def run(self, arguments: dict):

        return self.func(arguments)