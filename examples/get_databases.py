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
    get_databases = mitto.get_databases()
    print(get_databases)


if __name__ == "__main__":
    sys.exit(main())
