import logging
import pathlib
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    posadasJsonFile = pathlib.Path(__file__).parent / "posadas" / "posadas.json"
    if posadasJsonFile.exists():
        return func.HttpResponse(
            posadasJsonFile.read_text(),
            status_code=200,
            mimetype='application/json'
        )
    return func.HttpResponse(
        "posadas.json missing",
        status_code=503
    )
    
