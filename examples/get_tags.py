"""
Getting all jobs tags in Mitto instance.
"""
import os
import sys
import uuid

from dotenv import load_dotenv
from create_tag import main as created_tag
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
UUID = str(uuid.uuid4())
NAME = f"tag_{UUID}".replace("-", "_")
BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

TAG = {
    "name": NAME
}


def main(BASE_URL, API_KEY):
    """getting tags"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    create_tag = created_tag(TAG=TAG)  # noqa: F841# pylint: disable=W0612
    tags = mitto.get_tags()
    return tags


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY))