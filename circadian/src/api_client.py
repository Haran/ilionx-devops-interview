import datetime
import os
import sys
import jsonschema
import requests
import dataclasses
import dateutil.parser
from dotenv import load_dotenv
from .models.result import Result

DEFAULT_URL = 'https://api.sunrise-sunset.org/json'
DEFAULT_LAT = '50.930581'
DEFAULT_LNG = '5.780691'

DEFAULT_ERROR = 'API error'

SCHEMA = {
    "type": "object",
    "required": ["results"],
    "properties": {
        "results": {
            "type": "object",
            "required": ["sunrise", "sunset"],
            "properties": {
                "sunrise": {"type": "string"},
                "sunset": {"type": "string"},
            }
        },
    }
}


class ApiClient:
    @dataclasses.dataclass(frozen=True)
    class Params:
        lat: str = dataclasses.field(default_factory=lambda: os.getenv('LAT', DEFAULT_LAT))
        lng: str = dataclasses.field(default_factory=lambda: os.getenv('LNG', DEFAULT_LNG))

        def as_dict(self) -> dict:
            return {'lat': self.lat, 'lng': self.lng, 'formatted': '0'}

    def __init__(self):
        load_dotenv(os.path.join(os.path.dirname(sys.argv[0]), '.env'))
        self.params = self.Params()

    def fetch_data(self) -> Result:
        """
        :raises: AssertionError
        :raises: jsonschema.ValidationError
        :raises: requests.exceptions.ConnectionError
        :raises: dateutil.parser._parser.ParserError
        """
        request = self.__prepare_request()
        assert request.url is not None
        response = requests.get(request.url)

        self.__validate_response(response)
        sunrise, sunset = self.__parse_response(response)

        return Result(sunrise=sunrise, sunset=sunset)

    def __prepare_request(self) -> requests.PreparedRequest:
        request = requests.PreparedRequest()
        request.prepare_url(DEFAULT_URL, self.params.as_dict())
        return request

    @staticmethod
    def __parse_response(response: requests.models.Response) -> tuple[datetime.datetime, datetime.datetime]:
        json = response.json()
        sunrise = dateutil.parser.parse(json['results']['sunrise'])
        sunset = dateutil.parser.parse(json['results']['sunset'])
        return sunrise, sunset

    @staticmethod
    def __validate_response(response: requests.Response) -> None:
        assert response.ok is True, DEFAULT_ERROR
        jsonschema.validate(instance=response.json(), schema=SCHEMA)
