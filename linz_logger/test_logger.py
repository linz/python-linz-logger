"""
Tests for the hello() function.
"""

from structlog.testing import capture_logs

from .logger import get_log


def test_hello_without_name():
    """Test with no parameter."""
    assert get_log() is not None


def test_trace():
    with capture_logs() as cap_logs:
        get_log().trace("abc")
        assert cap_logs[0]["event"] == "abc"
        assert cap_logs[0]["log_level"] == "trace"
