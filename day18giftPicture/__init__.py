import logging
import json
import azure.functions as func
from __app__.SharedCode.cognitiveHelper import getImageTags
from __app__.SharedCode.slackHelper import NotifySlack



def main(myblob: func.InputStream) -> func.HttpResponse:
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    requiredTags = [
        'box',
        'gift wrapping',
        'ribbon',
        'present'
    ]
    try:
        tags = getImageTags(myblob.uri)
        if all(tag in tags for tag in requiredTags):
            NotifySlack(f"{myblob.name} if perfectly wrapped gift!")
        else:
            logging.info(f"tags: {tags}")
            NotifySlack(f"{myblob.name} if perfectly wrapped gift!")
    except OSError as e:
        logging.exception("Exception reading blob content...")
        NotifySlack(f"Exception occurred. Check logs {e.message}")

