import logging
import os
import json
import uuid
from azure.cosmos import exceptions, CosmosClient, PartitionKey
import azure.functions as func
from typing import Dict

logging.info("bootstrapping COSMOS DB connection...")
cosmosclient = CosmosClient.from_connection_string(os.environ["COSMOSDB_STRING"])
databaseName = 'day11'
logging.info("bootstrapping databse...")
database = cosmosclient.create_database_if_not_exists(id=databaseName)
containerName = 'wishes'
logging.info("bootstrapping databse container...")
CONTAINER = database.create_container_if_not_exists(
    id=containerName,
    partition_key=PartitionKey(path="/type"),
    offer_throughput=400
)

def getAllItems():
    global CONTAINER
    items = list(
        CONTAINER.query_items(
            'SELECT d.childname, d.description, d.type, d.address FROM wishes as d',
            enable_cross_partition_query=True
        )
    )
    return items

def newDbItem(item: Dict):
    global CONTAINER
    try:
        temp = CONTAINER.create_item(item)
        logging.info(temp)
    except Exception:
        logging.exception("Failed to update DB!")