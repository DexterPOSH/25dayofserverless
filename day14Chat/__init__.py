import logging
import pathlib
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    indexFile = pathlib.Path(__file__).parent / "index.html"
    return func.HttpResponse(
        body=indexFile.read_text(encoding='UTF-8'),
        status_code=200,
        headers={
            'Content-Type': 'text/html',
            'charset': 'utf-8'
        },
        mimetype='text/html'
    )
