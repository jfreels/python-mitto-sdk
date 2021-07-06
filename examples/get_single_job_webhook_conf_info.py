import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

job_id_str = input("Input id of job that you want to get webhook and conf: ")
job_id = int(job_id_str)

def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    webhook = mitto.get_job_webhooks(job_id=job_id)
    job_conf = mitto.get_job(job_id=job_id)
    conf = job_conf['conf'] 
    print(f"Job_webhook: {webhook}\n Job_conf: {conf}")


if __name__ == "__main__":
    sys.exit(main())
