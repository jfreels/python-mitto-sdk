import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

name = input("Input the name of SQL job(one word): ")

JOB = {
    "name": name,
    "title": f"[SQL]{name}",
    "type": "sql",
    "tags": [
        "sql"
    ],
    "conf": {
        "dbo": "postgresql://localhost/analytics",
        "sql": "select 1;",
        "parameters": {},
        "kwargs": {},
        "transaction": True,
        "split": False
    }
}


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    job = mitto.create_job(job=JOB)
    print(job)


if __name__ == "__main__":
    sys.exit(main())
