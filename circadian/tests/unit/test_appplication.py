import pytest
import dateutil.parser
from datetime import datetime
from ...src.application import make_decision

'''
list[
    tuple(
        data:     dict{'sunset': 'datetime string', 'sunrise': 'datetime string'},
        now:      datetime,
        expected: string
    )
]
'''
testdata_valid: list[tuple[datetime, datetime, datetime, str]] = [
    (
        # now is between sunrise and sunset
        dateutil.parser.parse('2024-02-22 06:34:45+00:00'),
        dateutil.parser.parse('2024-02-22 17:06:02+00:00'),
        dateutil.parser.parse('2024-02-22 11:00:00+00:00'),
        'OFF'
    ),
    (   # now==sunrise
        dateutil.parser.parse('2024-02-22 06:00:00+00:00'),
        dateutil.parser.parse('2024-02-22 17:00:00+00:00'),
        dateutil.parser.parse('2024-02-22 06:00:00+00:00'),
        'OFF'
    ),
    (   # now==sunset
        dateutil.parser.parse('2024-02-22 06:00:00+00:00'),
        dateutil.parser.parse('2024-02-22 17:00:00+00:00'),
        dateutil.parser.parse('2024-02-22 17:00:00+00:00'),
        'ON'
    ),
    (   # now after sunset
        dateutil.parser.parse('2024-02-22 06:34:45+00:00'),
        dateutil.parser.parse('2024-02-22 17:06:02+00:00'),
        dateutil.parser.parse('2024-02-22 19:00:00+00:00'),
        'ON'
    ),
    (   # now before sunrise, DST of 2023
        dateutil.parser.parse('2023-03-26 06:11:17+00:00'),
        dateutil.parser.parse('2023-03-26 18:35:32+00:00'),
        dateutil.parser.parse('2023-03-26 01:00:00+00:00'),
        'ON'
    ),
    (   # app started 1 sec before midnight, api response came 1 sec after
        dateutil.parser.parse('2023-03-27 06:11:17+00:00'),
        dateutil.parser.parse('2023-03-27 18:35:32+00:00'),
        dateutil.parser.parse('2023-03-26 23:59:59+00:00'),
        'ON'
    ),
]


@pytest.mark.parametrize("sunrise, sunset, now, expected", testdata_valid)
def test_decision(sunrise: datetime, sunset: datetime, now: datetime, expected: str) -> None:
    assert make_decision(sunrise, sunset, now) == expected
