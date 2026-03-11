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
        r = requests.get(f"https://uapis.cn/api/v1/misc/weather/?city={city}",timeout=5)
        data=r.json()
        return {
            "city":city,
            "weather":data["weather"],
            "temperature":data["temperature"]
        }