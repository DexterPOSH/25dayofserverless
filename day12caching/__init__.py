import logging
import requests
import os
import json
import azure.functions as func
from __app__.SharedCode.redisHelper import getValueFromCache, setValueInCache
from __app__.SharedCode.markdownHelper import convertMDToHTML
from __app__.SharedCode.githubHelper import fetchDataFromGist
from typing import Dict


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    friend = req.params.get('friendname')
    if not friend:
        try:
            req_body = req.get_json()
        except ValueError:
            logging.exception("friendname not specified in the JSON body")
            invalidInputObject = {
                'result': 'Property friendname missing in the route query or Json body'
            }
            return func.HttpResponse(
                json.dumps(invalidInputObject),
                status_code=400
            )
        else:
            friend = req_body.get('friendname')

    # fetch the HTML content from cache
    if getValueFromCache(friend):
        logging.info('cache hit...')
    else:
        # if not found then create the HTML and seed it in Cache
        logging.info('cache miss...')
        logging.info('fetch gist content...')
        gistContent = fetchDataFromGist(os.environ['GITHUB_GISTID'])
        fileHashTable = extractFileContent(gistContent)
        logging.info('seeding cache for missing info...')
        try:
            mdContent = fileHashTable[friend]
            setValueInCache(friend, convertMDToHTML(mdContent))
        except KeyError as notfound:
            logging.warn(notfound)
            return func.HttpResponse(
                '',
                status_code=204
            )

    # Now cache must have the HTML content, get from it
    
    bodyContent = getValueFromCache(friend)
    return func.HttpResponse(
        body=bodyContent,
        status_code=200,
        headers={
            'Content-Type': 'text/html'
        }
    )


def extractFileContent(contentObject: Dict) -> Dict:
    contentHashTable = {}
    for filename, filemeta in contentObject['files'].items():
        friendName = filename.split('.')[0]
        fileContent = filemeta['content']
        contentHashTable[friendName] = fileContent
    return contentHashTable
