import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
job_id = input(" Input a number of existing job that you want to get: ")

def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    job = mitto.get_job(job_id=job_id)
    print(job["id"], job["name"])


if __name__ == "__main__":
    sys.exit(main())
