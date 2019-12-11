import logging
import os
import json
import uuid
from azure.cosmos import exceptions, CosmosClient, PartitionKey
import azure.functions as func
from __app__.SharedCode.cosmosHelper import getAllItems


"""Entry point for GET|POST requests
    GET Request
        returns all the entries in the DB

    POST Request
        creates a new entry for th wish in the DB,
        The JSON body looks like:
    {
        "description": "wish to have a pony",
        "childname": "Joe",
        "address": "7th Baker street, London",
        "type": "animal"
    }
"""
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    returnBody, statusCode = GetAll()
    return func.HttpResponse(
        body=returnBody,
        status_code=statusCode
    )


def GetAll():
    items = getAllItems()
    if items:
        logging.info('Got response back')
        bodyString = json.dumps(items)
        return ( bodyString,200 )
    return ('', 200)

