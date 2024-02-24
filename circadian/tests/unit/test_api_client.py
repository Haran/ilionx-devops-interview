import os
import typing
import unittest
from unittest import mock

from dateutil.parser import ParserError
from jsonschema.exceptions import ValidationError

from ...src.models.result import Result
from ...src.api_client import ApiClient

testdata_broken1 = {"results": {"sunrise": ""}}
testdata_broken2 = {"results": {"sunrise": "asd", "sunset": "asd"}}

testdata_valid = {
    "results": {
        "sunrise": "2023-03-26T06:11:17+00:00",
        "sunset": "2023-03-26T18:35:32+00:00"
    },
    "status": "OK",
    "tzid": "UTC"
}


def mock_call(data, ok: bool = True) -> typing.Callable:
    class MockResponse:
        def __init__(self, json_data, status_code: int):
            self.ok = ok
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    def wrapper(_) -> MockResponse:
        return MockResponse(data, 200)

    return wrapper


class ApiClientTestCase(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mock_call(testdata_valid))
    def test_fetch_success(self, _):
        with mock.patch.dict(os.environ, {"URL": 'http://localhost'}):
            api_client = ApiClient()
            result = api_client.fetch_data()
            assert isinstance(result, Result)

    @mock.patch('requests.get', side_effect=mock_call(testdata_broken1))
    def test_fetch_broken_schema(self, _):
        with mock.patch.dict(os.environ, {"URL": 'http://localhost'}):
            api_client = ApiClient()
            with self.assertRaises(ValidationError) as _:
                api_client.fetch_data()

    @mock.patch('requests.get', side_effect=mock_call(testdata_broken2))
    def test_fetch_no_dates(self, _):
        with mock.patch.dict(os.environ, {"URL": 'http://localhost'}):
            api_client = ApiClient()
            with self.assertRaises(ParserError) as _:
                api_client.fetch_data()

    @mock.patch('requests.get', side_effect=mock_call(testdata_broken2, False))
    def test_fetch_no_json(self, _):
        with mock.patch.dict(os.environ, {"URL": 'http://localhost'}):
            api_client = ApiClient()
            with self.assertRaises(AssertionError) as _:
                api_client.fetch_data()


if __name__ == '__main__':
    unittest.main()
