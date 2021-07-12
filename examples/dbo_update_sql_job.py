import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto


load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB_ID = 45

DBO = "postrgesql://localhost/analytics"
INPUT_DBO = "postgres"

JOB_TYPE = "sql"


def main():
    mitto = Mitto(
         base_url=BASE_URL,
         api_key=API_KEY
    )
    job = mitto.get_job(job_id=JOB_ID)
    conf = job["conf"]
    conf["dbo"] = DBO
    job["conf"] = conf
    update_conf_dbo = mitto.update_job_conf(job_id=JOB_ID, job_conf=conf)
    print(f"Updating job dbo conf: {update_conf_dbo}")


if __name__ == "__main__":
    sys.exit(main())
