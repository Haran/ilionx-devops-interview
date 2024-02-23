from datetime import datetime

ERROR = "ERROR"
LIGHTS_ON = "ON"
LIGHTS_OFF = "OFF"


def make_decision(sunrise: datetime, sunset: datetime, now: datetime) -> str:
    if sunrise <= now < sunset:
        return LIGHTS_OFF
    return LIGHTS_ON
