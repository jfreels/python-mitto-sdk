import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

NAMED = "plugin_xsv__new_csv_job"


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    jobs = mitto.get_bulk_jobs(name=NAMED)
    print(jobs)


if __name__ == "__main__":
    sys.exit(main())
