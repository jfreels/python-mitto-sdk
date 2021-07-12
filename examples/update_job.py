import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB_ID = 52
UPDATE_JOB = {
  "title": "sql",
  "type": "sql",
  "markdown": "string",
  "schedule": {
    "type": "daily",
    "daily": {
      "minute": 0,
      "hour": 6,
      "ampm": "AM"
    },
  },
  "timeout": 0,
  "notify": 0,
  "delay": 0,
  "continue_on_error": True,
  "concurrency": 0,
  "conf": "string",
  "tags": [
    "string"
  ],
  "input": {},
  "output": {},
  "sdl": {},
  "steps": [
    "string"
  ]
}


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    update_job = mitto.update_job(job_id=JOB_ID, update_job_body=UPDATE_JOB)
    print(f"Updating job dbo conf: {update_job}")


if __name__ == "__main__":
    sys.exit(main())
