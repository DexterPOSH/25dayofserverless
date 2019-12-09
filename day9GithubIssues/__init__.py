import logging
import os
import requests
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info(req.method)
    logging.info(req.get_body())
    try:
        req_body = req.get_json()
        logging.info(req_body)
        action = req_body['action']
        issue = req_body['issue']
        if action == 'opened':
            logging.info("Got an action OPENED event. Commenting...")
            token = os.getenv('GITHUB_TOKEN')
            if token:
                logging.info('Found GitHubToken')
                commentOnIssue(issue['url'],issue['user']['login'], token)
            else:
                logging.warn('GitHub token not found. Nothing can be done!')
                return func.HttpResponse(status_code=501)
        else: 
            logging.info("Not an action OPENED event. Skipping...")
    except ValueError as ex:
        logging.exception('API invocation failed')
        return func.HttpResponse(status_code=400)
    return func.HttpResponse('commented', status_code=200)


def commentOnIssue(issueUrl: str, issueCreator: str, token: str):
    hashTable = {
        'Authorization': 'token {0}'.format(token)
    }
    payload = {
        'body': 'Thank you @{} for creating the issue. Happy new year!'.format(issueCreator)
    }
    commentUrl = '{0}/comments'.format(issueUrl)
    r = requests.post(url=commentUrl, headers=hashTable, data=json.dumps(payload))
    if r.status_code == 201:
        logging.info('GitHub issue updated.')
    else:
        logging.warn(r)
