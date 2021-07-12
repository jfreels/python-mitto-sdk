import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
JOB_ID = 46


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    single_status = mitto.get_single_job_status(job_id=JOB_ID)
    print(single_status)


if __name__ == "__main__":
    sys.exit(main())
