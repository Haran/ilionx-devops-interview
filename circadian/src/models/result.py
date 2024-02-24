import dataclasses
import dateutil.tz
from datetime import datetime


@dataclasses.dataclass(frozen=True)
class Result:
    sunrise: datetime
    sunset: datetime
    now: datetime = dataclasses.field(default_factory=lambda: datetime.now(dateutil.tz.tzutc()))
