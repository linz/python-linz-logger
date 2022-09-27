import os
import time
from dataclasses import asdict, replace
from enum import Enum
from functools import partial
from platform import node

import structlog
from structlog.contextvars import bind_contextvars, clear_contextvars, merge_contextvars, unbind_contextvars
from structlog.exceptions import DropEvent
from ulid import ULID

from linz_logger.ot_attributes import OpenTelemetryAttributes
from linz_logger.ot_resources import OpenTelemetryResourceHost


class Severity(Enum):
    """
    https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/logs/data-model.md#field-severitynumber
    """

    TRACE = 1
    DEBUG = 5
    INFO = 9
    WARN = 13
    ERROR = 17
    FATAL = 21


structlog.PrintLogger.trace = structlog.PrintLogger.msg
pid = os.getpid()
hostname = node()
ulid = str(ULID())
clear_contextvars()
current_severity: Severity = Severity.DEBUG
resources: OpenTelemetryResourceHost = OpenTelemetryResourceHost(host_name=hostname)
attributes: OpenTelemetryAttributes = OpenTelemetryAttributes()


def set_severity(severity: Severity):
    """
    Set the loggging level.
    All logs less than the given value will not be displayed.
    """
    global current_severity
    current_severity = severity


def set_contextvars(key_value: dict):
    """Set the context variables.

    Args:
        key_value (dict): A dictionnary of key-value pairs.
    """
    bind_contextvars(**key_value)


def remove_contextvars(keys):
    """Remove the context variables.

    Args:
        keys (list): A list of keys.
    """
    unbind_contextvars(*keys)


def set_resources(ctx: OpenTelemetryResourceHost) -> None:
    global resources
    resources = replace(resources, **asdict(ctx))


def severity_filter(_, __, event_dict: dict):
    """
    Silently drop logs lower than the set severity.
    """
    if event_dict.get("Severity", 0) < current_severity.value:
        raise DropEvent
    return event_dict


# This is a standard format for the function so it needs all three arguments
# Even thought we do not use them
# pylint: disable=unused-argument
def add_default_keys(current_logger, method_name: str, event_dict: dict):
    """
        Configure structlog to output aligning with the openTelemety Log Data Model format
    {
      "Timestamp": 1586960586000,
      "Attributes": {
        "http.status_code": 500,
        "http.url": "http://example.com",
        "my.custom.application.tag": "hello",
      },
      "Resource": {
        "service.name": "donut_shop",
        "service.version": "semver:2.0.0",
        "k8s.pod.uid": "1138528c-c36e-11e9-a1a7-42010a800198",
      },
      "TraceId": "f4dbb3edd765f620", // this is a byte sequence
                                     // (hex-encoded in JSON)
      "SpanId": "43222c2d51a7abe3",
      "SeverityText": "INFO",
      "SeverityNumber": 9,
      "Body": "20200415T072306-0700 INFO I like donuts"
    }
    """

    event_dict["SeverityText"] = Severity[method_name].name if Severity[method_name] else Severity.TRACE.name
    event_dict["SeverityNumber"] = Severity[method_name] if Severity[method_name] else Severity.TRACE
    event_dict["Timestamp"] = time.time_ns()
    event_dict["Attributes"] = asdict(attributes)
    event_dict["Resources"] = asdict(resources)
    event_dict["Attributes"]["msg"] = event_dict["event"]
    del event_dict["event"]
    return event_dict


structlog.configure(
    processors=[
        merge_contextvars,
        add_default_keys,
        severity_filter,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer(),
    ]
)


def get_log():
    """
    get a instance of the JSON logger
    """
    log = structlog.get_logger()
    log.trace = partial(trace, log)
    return log


def trace(self, event, **kw):
    """
    add trace level
    """
    return self._proxy_to_logger("trace", event, **kw)
