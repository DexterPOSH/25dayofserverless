import logging
import os
import pathlib
from textgenrnn import textgenrnn
import azure.functions as func

weightsFile = pathlib.Path(__file__).parent / 'textgenrnn_weights.hdf5'
TEXTGEN = textgenrnn(weightsFile)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    joke = newJoke()
    return func.HttpResponse(
        joke[0],
        status_code=200,
        headers= {
            'Content-Type': 'text/html'
        }
    )


def newJoke(temp : float = 0.5) -> str:
    global TEXTGEN
    return TEXTGEN.generate(temperature=temp, return_as_list=True)