"""
Getting all jobs in Mitto instance.
"""
import os
import sys
import uuid

from dotenv import load_dotenv
from create_job import main as created_job
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
UUID = str(uuid.uuid4())
NAME = f"sql_{UUID}".replace("-", "_")
TITLE = f"[SQL]{UUID}"
TYPE = "sql"
BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
JOB = {
  "name": NAME,
  "title": TITLE,
  "type": TYPE,
  "schedule": {
      "value": "daily",
      "type": "daily",
      "daily": {
          "minute": 0,
          "hour": 12,
          "ampm": "AM"
      },
      "hourly": None,
      "custom": None
  },
  "conf": {
    "dbo": "postgresql://localhost/analytics",
    "credentials": None,
    "sql": "select 1",
    "parameters": {},
    "kwargs": {},
    "transaction": True,
    "split": False
  }
}


def main(base_url=BASE_URL, api_key=API_KEY, job=JOB):
    """getting all jobs"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    job = created_job(job=job)  # noqa: F841#pylint: disable=W0612
    jobs = mitto.get_jobs()
    return jobs


if __name__ == "__main__":
    sys.exit(main(base_url=BASE_URL, api_key=API_KEY, job=JOB))
