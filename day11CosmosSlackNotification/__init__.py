import logging
import requests
import os
import json
import azure.functions as func


def main(documents: func.DocumentList) -> str:
    if documents:
        logging.info(documents)
        for document in documents:
            NotifySlack(
                os.environ['SLACK_WEBHOOK'],
                'new wish added by {0}, type {1}, description: {2}. Deliver at {3}'.format(
                    document['childname'],
                    document['type'],
                    document['description'],
                    document['address']
                )
            )
    
def NotifySlack(slackUrl: str, msg: str):
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