import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
TAGS_ID = 1


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    tags = mitto.get_tags(tags_id=TAGS_ID)
    print(tags)


if __name__ == "__main__":
    sys.exit(main())
