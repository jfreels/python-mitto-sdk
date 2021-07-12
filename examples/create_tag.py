import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

TAGS = {
    "name": "diffpiff"
}


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    create_tag = mitto.create_tags(tags=TAGS)
    print(f"{create_tag} is succesfully created")


if __name__ == "__main__":
    sys.exit(main())
