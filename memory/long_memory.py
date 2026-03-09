import json
import os
import re
from core.message import Message
from memory.base import BaseMemory
class LongMemory(BaseMemory):

    def __init__(self, path="memory/memory_db.json"):

        self.path = path

        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump({}, f)

    def _load(self):

        with open(self.path, "r",encoding="utf-8") as f:
            return json.load(f)

    def _save(self, data):

        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2, separators=(',', ': '))

    def extract(self, text):
        facts = {}
        name_match = re.search(r"我叫(\w+)", text)
        if name_match:
            facts["name"] = name_match.group(1)
        city_match = re.search(r"我在(\w+)", text)
        if city_match:
            facts["city"] = city_match.group(1)
        return facts


    def add(self,input:Message):
        data = self._load()
        facts = self.extract(input.content)
        for k, v in facts.items():
            data[k] = v
        self._save(data)

    def get(self):
        data=self._load()
        if not data:
            return ""  # 无记忆时返回空字符串
        
        # 构建格式化字符串
        info_parts = []
        if "name" in data:
            info_parts.append(f"姓名：{data['name']}")
        if "city" in data:
            info_parts.append(f"城市：{data['city']}")
        
        return "，".join(info_parts)

    def clear(self):
        pass

        