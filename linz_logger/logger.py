import os
from datetime import datetime

import structlog

# Convert to pinojs standard level numbers
NAME_TO_LEVEL = {
    "critical": 60,
    "exception": 50,
    "error": 50,
    "warn": 40,
    "warning": 40,
    "info": 30,
    "debug": 20,
    "notset": 10,
}


pid = os.getpid()

# This is a standard format for the function so it needs all three arguments
# Even thought we do not use them
# pylint: disable=unused-argument
def add_default_keys(current_logger, method_name: str, event_dict: dict):
    """
    Configure structlog to output the same format as pinojs
    {
        "level": 30,
        "time": 1571696532994,
        "pid": 10671,
        "hostname": "Ubuntu1",
        "id": "01DQR6KQG0K60TP4T1C4VC5P74",
        "msg": "SomeMessage",
        "v": 1
    }
    """
    event_dict["level"] = NAME_TO_LEVEL[method_name]

    # Time needs to be in ms
    event_dict["time"] = int(datetime.utcnow().timestamp() * 1000)

    # Standard keys that need to be added
    event_dict["v"] = 1
    event_dict["pid"] = pid

    # Remap event -> msg
    event_dict["msg"] = event_dict["event"]
    del event_dict["event"]
    return event_dict


structlog.configure(
    processors=[
        add_default_keys,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer(),
    ],
    context_class=structlog.threadlocal.wrap_dict(dict),
)


def get_log():
    """
    get a instance of the JSON logger
    """
    return structlog.get_logger()
