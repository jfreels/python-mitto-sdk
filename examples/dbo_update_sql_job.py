import os
import sys
import json

import hjson
import requests
from dotenv import load_dotenv

from mitto_sdk import Mitto


load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB_ID_STR = input("Input id of SQL job that you want to update: ")
JOB_ID = int(JOB_ID_STR) 

dbo = input("Input new dbo link to update sql job(default - postgresql://localhost/analytics):\n") or "postrgesql://localhost/analytics"
INPUT_DBO = "postgres"

JOB_TYPE = "sql"


def main():
    mitto = Mitto(
         base_url=BASE_URL,
   	 api_key=API_KEY
    )
   
    job = mitto.update_job_conf_dbo(job_id=JOB_ID)
    conf = job["conf"]
    conf["dbo"] = dbo
    job["conf"] = conf
    res = requests.patch(url=f"{BASE_URL}/api/v2/jobs/{JOB_ID}?API_KEY={API_KEY}", json = job)
    print(f"Updating job dbo conf: {JOB_ID}, {dbo}")


if __name__ == "__main__":
    sys.exit(main())


