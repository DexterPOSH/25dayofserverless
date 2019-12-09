import logging

import azure.functions as func
import requests

# DefaultEndpointsProtocol=https;AccountName=dexfuncappstore;AccountKey=4/wyhEqMjp1rWdJ+77KxmtjEPSAS9L7vbUFjVBL9ob3Gd0ZLnuy0nbm6lfSF737Hl3hQDC9gPk2Cz/eXM8+a7A==;EndpointSuffix=core.windows.net

def main(req: func.HttpRequest, outputBlob: func.Out[bytes]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)
    repoInfo = req_body.get('repository')
    logging.info("repoInfo)
    commitInfo = req_body.get('head_commit')
    logging.info(commitInfo)
    baseUrl = "{0}/raw/master/".format(repoInfo["html_url"])
    for itemAdded in commitInfo['added']:
        logging.info("Item added - {0}".format(itemAdded))
        if itemAdded.endswith('.png'):
            logging.info('Item added with .png suffix. Processing...')
            itemUrl = baseUrl + itemAdded
            logging.info("Item Url - {0}".format(itemUrl))
            fileName = itemAdded.split('/')[-1]
            # download the file locally and then upload to blob
            try:
                requestObject = requests.get(itemUrl, allow_redirects=True)
                outputBlob.set(requestObject.content)
            except Exception as ex:
                logging.fatal(ex)
    return func.HttpResponse(fileName, status_code=200)