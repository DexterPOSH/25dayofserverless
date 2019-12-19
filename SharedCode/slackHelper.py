import requests
import json
import os
import logging

def NotifySlack(msg: str):
    slackUrl = os.environ['SLACK_WEBHOOK']
    payload = {
        'text': msg
    }
    hashTable = {
        'Content-type': 'application/json'
    }
    r = requests.post(url=slackUrl, headers=hashTable, data=json.dumps(payload))
    if r.status_code == 201:
        logging.info('Slack channel notified!')
    else:
        logging.warn(r)