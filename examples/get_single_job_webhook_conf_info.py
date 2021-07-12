import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB_ID = 46


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    webhook = mitto.get_job_webhooks(job_id=JOB_ID)
    job_conf = mitto.get_job(job_id=JOB_ID)
    conf = job_conf['conf']
    print(f"Job_webhook: {webhook}\n Job_conf: {conf}")


if __name__ == "__main__":
    sys.exit(main())
