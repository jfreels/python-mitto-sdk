import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
JOB_ID = 29


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    jobs = mitto.delete_job(job_id=JOB_ID)
    print(f'{jobs}\n If you see <Response [204]> message',
          f'job {JOB_ID} succesfuly deleted')


if __name__ == "__main__":
    sys.exit(main())
