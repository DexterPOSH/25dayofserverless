import pytest
import json
import pathlib
from jsonschema import validate

def test_posadas_exists():
    posadasJsonFile = pathlib.Path(__file__).parent / "posadas.json"
    assert posadasJsonFile.exists() == True

def assert_valid_schema():
    schemaFilePath = pathlib.Path(__file__).parent / "posadas.schema.json"
    schema = json.loads(schemaFilePath.read_text())
    posadasJsonFile = pathlib.Path(__file__).parent / "posadas.json"
    data = json.loads(posadasJsonFile.read_text())
    return validate(data, schema)

