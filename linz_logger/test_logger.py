import json
import os

from .logger import Severity, get_log, remove_contextvars, set_contextvars, set_severity


def test_hello_without_name():
    """Test with no parameter."""
    assert get_log() is not None


def test_trace(capsys):
    """Test trace level"""
    set_severity(Severity.TRACE)
    get_log().trace("abc")
    stdout, _ = capsys.readouterr()
    log = json.loads(stdout)
    assert log["SeverityText"] == Severity.TRACE.name
    assert log["msg"] == "abc"


def test_trace_at_debug_level(capsys):
    """Test trace level outputs nothing when log set to debug"""
    set_severity(Severity.DEBUG)
    get_log().trace("abc")
    stdout, _ = capsys.readouterr()
    assert stdout == ""


def test_timestamp(capsys):
    """Test timestamp is actually a timestamp"""
    set_severity(Severity.TRACE)

    systime = int(os.popen("date +%s").read()) * 1000
    get_log().trace("abc")
    stdout, _ = capsys.readouterr()
    log = json.loads(stdout)

    assert log["Timestamp"] - systime < 1000
