import requests

from config import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN,
    ZAPI_CLIENT_TOKEN
)


class ZApiClient:

    def __init__(self):

        self.url = (
            f"https://api.z-api.io/"
            f"instances/{ZAPI_INSTANCE_ID}"
            f"/token/{ZAPI_TOKEN}"
            f"/send-text"
        )

        self.headers = {
            "Client-Token": ZAPI_CLIENT_TOKEN,
            "Content-Type": "application/json"
        }

    def send_message(
        self,
        phone: str,
        message: str
    ) -> requests.Response:

        payload = {
            "phone": phone,
            "message": message
        }

        return requests.post(
            self.url,
            json=payload,
            headers=self.headers,
            timeout=30
        )