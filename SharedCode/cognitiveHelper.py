from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import logging
import os
import requests
from typing import List


# Add your Computer Vision subscription key to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    logging.warn("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
# Add your Computer Vision endpoint to your environment variables.
if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
else:
    logging.warn("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")

COMPUTERVISION_CLIENT = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False

def getImageDescription(imgUrl: str) -> List:
    global COMPUTERVISION_CLIENT
    description_results = COMPUTERVISION_CLIENT.describe_image(imgUrl)
    return [item.text for item in description_results.captions]

def getImageTags(imgUrl: str) -> List:
    global COMPUTERVISION_CLIENT
    tag_results = COMPUTERVISION_CLIENT.tag_image(imgUrl)
    return [tag.name for tag in tag_results.tags]