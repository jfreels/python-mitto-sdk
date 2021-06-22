import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB_ID_STR = input("Input id of job that you want to update: ")
JOB_ID = int(JOB_ID_STR) 

sql_command = input("Input sql command that you want to input into configuration:\n ")

JOB_CONF = {
    "dbo": "postgresql://localhost/analytics",
    "sql": sql_command,
    "parameters": {},
    "kwargs": {},
    "transaction": True,
    "split": False
}


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    updated_job = mitto.update_job_conf(job_id=JOB_ID, job_conf=JOB_CONF)
    print(updated_job)


if __name__ == "__main__":
    sys.exit(main())
