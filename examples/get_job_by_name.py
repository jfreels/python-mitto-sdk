import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
name = input("Input name of job that you want to get info: ")

def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    jobs = mitto.get_bulk_jobs(name=name)
    print(jobs)


if __name__ == "__main__":
    sys.exit(main())

