"""
Getting job by existing name.
"""
import os
import sys
import uuid

from dotenv import load_dotenv
from create_bulk_job import main as created_bulk_job  # noqa: E501# pylint: disable;E0401
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
UUID = str(uuid.uuid4())
NAME = f"bulk_{UUID}".replace("-", "_")
TITLE = f"[BULK]{UUID}"
TYPE = "bulk"

BULK_JOB = [
  {
    "name": NAME,
    "title": TITLE,
    "type": TYPE,
    "markdown": "string",
    "schedule": {
      "type": "daily",
      "daily": {
        "minute": 0,
        "hour": 12,
        "ampm": "AM"
      },
      "hourly": None,
      "custom": None
    },
    "timeout": 0,
    "notify": 0,
    "delay": 0,
    "continue_on_error": True,
    "concurrency": 0
  }
]


def main(BASE_URL, API_KEY):
    """
    Request to API with current configurations.
    """
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    create_bulk_job = created_bulk_job(BULK_JOB=BULK_JOB)
    results = create_bulk_job["results"]
    jobs = mitto.get_bulk_jobs(results)
    return jobs


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY))
