import logging
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
    "trace": 5,
}

structlog.stdlib.TRACE = TRACE = 5
structlog.stdlib._NAME_TO_LEVEL["trace"] = TRACE
structlog.stdlib._LEVEL_TO_NAME[TRACE] = "trace"


def trace(self, msg, *args, **kw):
    return self.log(TRACE, msg, *args, **kw)


structlog.stdlib._FixedFindCallerLogger.trace = trace
structlog.stdlib.BoundLogger.trace = trace

logging.basicConfig(
    level=int(os.environ.get("LOGLEVEL", TRACE)),
    format=os.environ.get("LOGFORMAT", "%(levelname)-8s= %(asctime)-15s = %(message)s"),
)

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.render_to_log_kwargs,
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logging.addLevelName(TRACE, "TRACE")


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
