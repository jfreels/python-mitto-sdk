"""Updating a webhook"""
import os
import sys
import json

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

OLD_WEBHOOK = "https://hooks.slack.com/services/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"  # noqa: E501
WEBHOOK = "https://hooks.slack.com/services/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"  # noqa: E501

with open("test_section.json", "r") as f:
     data = json.load(f)

def main():
    """
    Updating all webhooks in Mitto instance to defined webhook
    """
    with open("test_section.json") as f:
     data = json.load(f)
     for response in data:
         print(response["name"])
         BASE_URL = response["url"]
         API_KEY = response["apikey"]
         mitto = Mitto(
             base_url=BASE_URL,
             api_key=API_KEY
         )
         update_webhook_list = []
         webhooks = mitto.get_webhooks()
         for n in webhooks:
             webhook = n
             webhook_id = webhook["id"]
             if webhook["url"] == OLD_WEBHOOK:
                 webhook_url = webhook["url"]
                 webhook_url = WEBHOOK
                 webhook["url"] = webhook_url
                 update_webhook = mitto.update_a_webhook(webhook_id=webhook_id, webhook=webhook)  # noqa: E501
                 update_webhook_list.append(update_webhook)
         return update_webhook_list


if __name__ == "__main__":
    sys.exit(main())
