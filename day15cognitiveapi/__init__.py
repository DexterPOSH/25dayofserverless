import logging
import json
import azure.functions as func
from azure.cognitiveservices.vision.computervision.models._models_py3 import ComputerVisionErrorException
from __app__.SharedCode.cognitiveHelper import getImageDescription, getImageTags, is_url_image


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    if url:
        if is_url_image(url):
            logging.info('guessed from content header that the URL is for an image...')
            returnObject = {}
            try:
                returnObject["description"] = getImageDescription(url)
                returnObject["tags"] = getImageTags(url)
            except ComputerVisionErrorException as e:
                return func.HttpResponse(
                    e.message,
                    status_code=400
                )
            # bodyString = json.dumps(returnObject)
            return func.HttpResponse(
                body=json.dumps(returnObject),
                status_code=200,
                mimetype='application/json'
            )
        else:
            logging.warn('guessed from content header that the URL is NOT for an image...')
            return func.HttpResponse(
                body="URL specified is wrong, not pointing to an img (png/jpeg/jpg)",
                status_code=400
            )
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
