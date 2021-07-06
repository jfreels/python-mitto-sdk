import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

name = input("Input a name of creating job(one word): ")
title = input("Input a title of creating job(one word): ")
type = input(" Input a type of creating job(one word): ")
tags = input("Input a tags of creating job(one word): ")

JOB = {
    "name": name,
    "title": title,
    "type": type,
    "tags": [
        tags
    ],
    "conf": {}
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
