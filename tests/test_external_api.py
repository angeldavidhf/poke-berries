import os
import requests
import pytest
from unittest.mock import patch, Mock
from fastapi import HTTPException

from app.api.external_api import call_external_api

os.environ["POKEAPI_BASE_URL"] = "https://pokeapi.co/api/v2"
os.environ["POKEAPI_BERRIES_ENDPOINT"] = "/berry"


def test_call_external_api():
    berry_data = call_external_api()
    assert isinstance(berry_data, list)

    first_berry = berry_data[0]
    expected_keys = ['growth_time',
                     'id',
                     'name',
                     'max_harvest',
                     'size',
                     'smoothness',
                     'soil_dryness',
                     'natural_gift_power']
    assert all(key in first_berry for key in expected_keys)

    del os.environ["POKEAPI_BASE_URL"]
    del os.environ["POKEAPI_BERRIES_ENDPOINT"]


def test_call_external_api_error():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Error")
        with pytest.raises(HTTPException):
            call_external_api()

