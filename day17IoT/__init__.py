import logging
import json
import azure.functions as func
from __app__.SharedCode.twitterHelper import sendTweet


def main(event: func.EventHubEvent):
    logging.info('Python HTTP trigger function processed a request.')
    messages = json.loads(event.get_body().decode('utf-8'))
    sum_temp = 0
    no_count = 0
    for telemetry in messages:
        temperature = telemetry.get('temperature')
        if validateTemperature(temperature):
            sum_temp += temperature
            no_count += 1
    
    average_temp = sum_temp / no_count
    if isTemperatureSuitable(average_temp):
        sendTweet("Temperature is {0}, perfect time to hit the beach".format(average_temp))
    else:
        logging.info("temperature is not suitable - {0}".format(average_temp))


def validateTemperature(temperature):
    if temperature is not None and not -40 <= temperature <= 80:
        return False
    return True


def isTemperatureSuitable(temp):
    if  31 <= temp <= 38 and temp:
        return True
    return False