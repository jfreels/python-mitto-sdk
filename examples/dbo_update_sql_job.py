"""
Updating dbo configuration on existing sql job in Mitto instance.
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

DBO = "postrgesql://localhost/analytics"
INPUT_DBO = "postgres"

JOB_TYPE = "sql"


def main(BASE_URL, API_KEY, DBO):
    """dbo updating"""
    mitto = Mitto(
         base_url=BASE_URL,
         api_key=API_KEY
    )
    job = created_job(JOB=JOB)
    print(job)
    job_id = job["id"]
    get_job = mitto.get_job(job_id=job_id)
    conf = get_job["conf"]
    conf["dbo"] = DBO
    get_job["conf"] = conf
    update_conf_dbo = mitto.update_job_conf(job_id=job_id, job_conf=conf)
    return update_conf_dbo


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY, DBO))
