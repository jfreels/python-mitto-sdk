import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

NEW_CREDS = {
    "name": "new creds",
    "type": "sql",
    "data": {}
}


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    create_creds = mitto.create_credentials(creds=NEW_CREDS)
    print(f"{create_creds} is succesfully created")


if __name__ == "__main__":
    sys.exit(main())
