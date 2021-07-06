import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
tags_id_str = input("Input tag_id of job that you want to get tags: ")
tags_id = int(tags_id_str)

def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    tags = mitto.get_tags(tags_id=tags_id)
    print(tags)


if __name__ == "__main__":
    sys.exit(main())
