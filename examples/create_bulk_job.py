import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

name = input("Input a name of creating bulk job(one word): ")
title = input("Input a title of creating bulk job(one word): ")
typel = input("Input a type of creating bulk job(one word): ")
tags = input(" Input a tags of creating bulk job(one word): ")

BULK_JOB = [{
    "name": name,
    "title": title,
    "type": typel,
    "tags": [
      tags
    ]
}]


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    bulk_job = mitto.create_bulk_jobs(bulk_job=BULK_JOB)
    print(bulk_job)


if __name__ == "__main__":
    sys.exit(main())
