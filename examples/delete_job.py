import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
JOB_ID_STR = input("Input id of job that you want to delete: ")
JOB_ID = int(JOB_ID_STR)

def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    jobs = mitto.delete_job(job_id=JOB_ID)
    type(jobs)
    dir(jobs)
    print(f"{jobs}\n If you see 'response 204' message, job {JOB_ID} succesfuly deleted")


if __name__ == "__main__":
    sys.exit(main())
