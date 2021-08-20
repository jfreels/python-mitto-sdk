"""Updating a webhook"""
import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
OLD_WEBHOOK = "https://hooks.slack.com/services/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"  # noqa: E501
WEBHOOK = "https://hooks.slack.com/services/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"  # noqa: E501


def main(BASE_URL, API_KEY, WEBHOOK, OLD_WEBHOOK):
    """
    Updating all webhooks in Mitto instance to defined webhook
    """
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
    sys.exit(main(BASE_URL, API_KEY, WEBHOOK, OLD_WEBHOOK))
