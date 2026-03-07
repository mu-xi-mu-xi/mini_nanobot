from tools.base import Tool
import requests

class WeatherTool(Tool):
    def __init__(self):
        super().__init__(
            name="weather",
            description="Get the current weather for a given location",
            parameters={
                "city":{
                    "type":"string",
                    "description":"City Name"
                }
            }
        )

    def run(self,arguments:dict)->str:
        city=arguments["city"]
        r = requests.get(f"https://wttr.in/{city}?format=j1")
        data=r.json()
        return {
            "city":city,
            "weather":data["current_condition"][0]["temp_C"]
        }