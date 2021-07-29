"""
Updating schedule of existing Mitto job.
"""
import os
import sys

from dotenv import load_dotenv
from get_job_schedule import main as get_schedule
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")


SCHEDULE = {
    "value": "daily",
    "type": "daily",
    "daily": {
      "minute": 0,
      "hour": 6,
      "ampm": "AM"
    },
    "hourly": None,
    "custom": None
}


def main(BASE_URL, API_KEY, SCHEDULE):
    """updating job`s schedule"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    get_sch = get_schedule(BASE_URL, API_KEY)
    sch_id = get_sch["id"]
    get_sch['schedule'] = SCHEDULE
    post_schedule = mitto.update_job_schedule(job_id=sch_id, job_schedule=get_sch)  # noqa: E501
    return post_schedule


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY, SCHEDULE))
