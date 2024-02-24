from datetime import datetime
from ...src.models.result import Result


def test_model_creation():
    subject = Result(sunset=datetime.now(), sunrise=datetime.now())
    assert isinstance(subject.sunrise, datetime)
    assert isinstance(subject.sunset, datetime)
    assert isinstance(subject.now, datetime)
