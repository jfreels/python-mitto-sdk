import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
WEBHOOK_ID_STR = input("Input id of webhook that you want to delete: ")
WEBHOOK_ID = int(WEBHOOK_ID_STR)


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    webhooks = mitto.delete_webhook(webhook_id=WEBHOOK_ID)
    print(f"{webhooks}\n If you see '<Response [204]>' message, webhook {WEBHOOK_ID} succesfuly deleted")


if __name__ == "__main__":
    sys.exit(main())
