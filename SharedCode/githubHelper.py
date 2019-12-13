import requests
import json
from typing import Dict

def fetchDataFromGist(gistId: str) -> Dict:
    gistUrl = "https://api.github.com/gists/{0}".format(gistId)
    response = requests.get(
        url=gistUrl
    )
    return json.loads(response.content)