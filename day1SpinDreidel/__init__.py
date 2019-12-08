import logging
import random
import azure.functions as func

choices = ['נ', 'ג', 'ה', 'ש']

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info('generating a random choice')
    return random.choice(choices)