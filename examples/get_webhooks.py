import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    webhooks = mitto.get_webhooks()
    for webhook in webhooks:
        print(webhook["id"], webhook["url"], webhook["method"], webhook["event_type"], webhook["content_type"], webhook["body"], webhook["enabled"], webhook["created_at"], webhook["updated_at"])


if __name__ == "__main__":
    sys.exit(main())
