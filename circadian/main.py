from jsonschema import ValidationError
from dateutil.parser import ParserError
from requests.exceptions import ConnectionError
from src.api_client import ApiClient
from src.application import make_decision, ERROR


if __name__ == '__main__':
    try:
        result = ApiClient().fetch_data()
        print(make_decision(result.sunrise, result.sunset, result.now))
    except (AssertionError, ValidationError, ConnectionError, ParserError):
        print(ERROR)
