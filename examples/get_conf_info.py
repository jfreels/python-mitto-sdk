"""
Getting configuration info of existing job in Mitto instance.
"""
import sys
import os
import uuid

from dotenv import load_dotenv
from create_sql_job import main as created_sql
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
UUID = str(uuid.uuid4())
JOB_TYPE = "sql"
INPUT_DBO_LIKE = "postgresql"
NAME = f"sql_{UUID}".replace("-", "_")
TITLE = f"[SQL]{UUID}"
BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
SQL_JOB = {
  "name": NAME,
  "title": TITLE,
  "type": "sql",
  "conf": {
    "input": {},
    "output": {
      "dbo": "postgresql://localhost/analytics",
      "schema": "",
      "tablename": "cogs",
      "use": "call:mitto.iov2.db#todb"
    }
  }
}


def main(BASE_URL, API_KEY):
    """show matching jobs"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    sql_job = created_sql(SQL_JOB=SQL_JOB)
    print(sql_job)
    jobs = mitto.get_jobs(job_type=JOB_TYPE)
    print(".\n.\n.\n.\n.\nJobs conf on jobs with defined job type:\n")
    for job in jobs:
        job_id = job['id']
        job_conf = mitto.get_job(job_id=job_id)
        conf = job_conf['conf']
        print(f"JOB ID: {job_id} - JOB CONF: {conf}")


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY))
