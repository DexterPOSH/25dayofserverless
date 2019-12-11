import logging
import os
import json
import uuid
from azure.cosmos import exceptions, CosmosClient, PartitionKey
import azure.functions as func
from __app__.SharedCode.cosmosHelper import newDbItem

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    reqObject = req.get_json()
    if (
        reqObject['childname'] and
        reqObject['description'] and
        reqObject["type"] and
        reqObject["address"]
    ):
        try:
            newDbItem(
                {
                    'childname': reqObject['childname'],
                    'description': reqObject['description'],
                    'type': reqObject['type'],
                    'address': reqObject['address'],
                    'id': str(uuid.uuid4())
                }
            )
            return func.HttpResponse(
                "",
                status_code=201
            )
        except Exception as ex:
            logging.exception('Creating the item in the container failed.')
            return func.HttpResponse(
                "InternalServerError",
                status_code=500
            )
    else:
        logging.warn("JSON body should have childname, description, type & id fields")
        return func.HttpResponse(
            "JSON body should have childname, description, type & id fields",
            status_code=400
        )

