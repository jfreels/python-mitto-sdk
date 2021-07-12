import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB_ID = 46

SCHEDULE = {
    "value": "continuous",
    "type": "continuous",
    "daily": None,
    "hourly": None,
    "custom": None
}


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    job_s = mitto.update_job_schedule(job_id=JOB_ID, job_schedule=SCHEDULE)
    job_schedule = job_s['schedule']
    print(job_schedule)


if __name__ == "__main__":
    sys.exit(main())
