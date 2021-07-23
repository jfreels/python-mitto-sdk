# python-mitto-sdk
Python Mitto SDK

## Overview:

Python library to interact with Mitto's API.

## Installation:
```python
pip install python-mitto-sdk
```

## Changing path to src for testing python-mitto-sdk package:
```cmd
export PYTHONPATH=./src
```

## Creating .env file with your $MITTO_BASE_URL and $MITTO_API_KEY:
```cmd
cd /path/to/your/python-mitto-sdk/examples && echo "MITTO_BASE_URL=https://your-mitto.zuarbase.net">.env && echo "MITTO_API_KEY=<YOUR_API_KEY>">>.env
```

## Usage:
```python
# What's my Mitto version?
from mitto_sdk import Mitto

BASE_URL = "https://{mitto_url}"
API_KEY = ""

mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

about = mitto.get_about()
version = about["version"]
print(version)
```
