import json
import os

from linz_logger.ot_attributes import OpenTelemetryAttributes
from linz_logger.ot_resources import OpenTelemetryResource

from .logger import Severity, get_log, set_attributes, set_resources, set_severity


def test_hello_without_name():
    """Test with no parameter."""
    assert get_log() is not None


def test_trace(capsys):
    """Test trace level"""
    set_severity(Severity.TRACE)
    get_log().trace("abc", "logStarted")
    stdout, _ = capsys.readouterr()
    log = json.loads(stdout)
    assert log["SeverityText"] == Severity.TRACE.name
    assert log["Attributes"]["msg"] == "abc"


def test_debug(capsys):
    """Test debug level"""
    set_severity(Severity.DEBUG)
    get_log().debug("abc")
    stdout, _ = capsys.readouterr()
    log = json.loads(stdout)
    assert log["SeverityText"] == Severity.DEBUG.name
    assert log["Attributes"]["msg"] == "abc"


def test_warn(capsys):
    """Test warn level"""
    set_severity(Severity.WARN)
    get_log().warn("abc")
    stdout, _ = capsys.readouterr()
    log = json.loads(stdout)
    assert log["SeverityText"] == Severity.WARN.name
    assert log["Attributes"]["msg"] == "abc"


def test_trace_at_debug_level(capsys):
    """Test trace level outputs nothing when log set to debug"""
    set_severity(Severity.DEBUG)
    get_log().trace("abc", "logStarted")
    stdout, _ = capsys.readouterr()
    assert stdout == ""


def test_timestamp(capsys):
    """Test timestamp is actually a timestamp"""
    set_severity(Severity.TRACE)

    systime = int(os.popen("date +%s").read()) * 10000000000
    get_log().trace("abc", "logStarted")
    stdout, _ = capsys.readouterr()
    log = json.loads(stdout)

    assert log["Timestamp"] - systime < 1000


def test_set_resources(capsys):
    """Test setting resources"""
    set_resources(OpenTelemetryResource(host_ip="192.168.0.2"))
    get_log().trace("abc", "logStarted")
    stdout, _ = capsys.readouterr()
    log = json.loads(stdout)

    assert log["Resources"]["host.ip"] == "192.168.0.2"


def test_set_attributes(capsys):
    """Test setting resources"""
    set_attributes(OpenTelemetryAttributes(error_message="test error"))
    get_log().debug("abc")
    stdout, _ = capsys.readouterr()
    log = json.loads(stdout)

    assert log["Attributes"]["error.message"] == "test error"
