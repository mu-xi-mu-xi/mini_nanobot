# channels/feishu.py
import os
from fastapi import FastAPI, Request
import requests
from core.message import Message
from dotenv import load_dotenv
load_dotenv()

class FeishuChannel:

    def __init__(self, agent):
        self.agent = agent
        self.app = FastAPI()

        self.app_id = os.getenv("app_id")
        self.app_secret = os.getenv("app_secret")

        self._register_routes()

    def _register_routes(self):

        @self.app.post("/feishu")
        async def receive(req: Request):

            data = await req.json()

            # 飞书URL验证
            if data.get("type") == "url_verification":
                return {"challenge": data["challenge"]}

            event = data.get("event", {})
            message = event.get("message", {})
            sender = event.get("sender", {})

            message_type = message.get("message_type")

            if message_type != "text":
                return {"msg": "only support text"}

            # 飞书content是字符串，需要解析
            content_str = message.get("content")
            content_json = json.loads(content_str)

            text = content_json.get("text")

            open_id = sender.get("sender_id", {}).get("open_id")

            if not text:
                return {"msg": "empty"}

            # 构造Agent Message
            user_msg = Message(role="user", content=text)

            # 调用Agent
            response = self.agent.run(user_msg)

            # 回复飞书
            self.send_message(open_id, response)

            return {"ok": True}

    def get_tenant_access_token(self):

        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"

        res = requests.post(url, json={
            "app_id": self.app_id,
            "app_secret": self.app_secret
        })

        return res.json()["tenant_access_token"]

    def send_message(self, open_id: str, text: str):

        token = self.get_tenant_access_token()

        url = "https://open.feishu.cn/open-apis/im/v1/messages"

        headers = {
            "Authorization": f"Bearer {token}"
        }

        params = {
            "receive_id_type": "open_id"
        }

        payload = {
            "receive_id": open_id,
            "msg_type": "text",
            "content": json.dumps({
                "text": text
            })
        }

        requests.post(url, headers=headers, params=params, json=payload)