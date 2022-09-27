# Python LINZ Logger

[![GitHub Actions Status](https://github.com/linz/python-linz-logger/workflows/Build/badge.svg)](https://github.com/linz/python-linz-logger/actions)
[![Kodiak](https://badgen.net/badge/Kodiak/enabled?labelColor=2e3a44&color=F39938)](https://kodiakhq.com/)
[![Dependabot Status](https://badgen.net/badge/Dependabot/enabled?labelColor=2e3a44&color=blue)](https://github.com/linz/python-linz-logger/network/updates)
[![License](https://badgen.net/github/license/linz/python-linz-logger?labelColor=2e3a44&label=License)](https://github.com/linz/python-linz-logger/blob/master/LICENSE)
[![Conventional Commits](https://badgen.net/badge/Commits/conventional?labelColor=2e3a44&color=EC5772)](https://conventionalcommits.org)
[![Code Style](https://badgen.net/badge/Code%20Style/black?labelColor=2e3a44&color=000000)](https://github.com/psf/black)

## Why?

[OpenTelemetry Log Data Model](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/logs/data-model.md)

```json
{
  "timestamp": 1586960586000,
  "attributes": {
    "http.status_code": 500,
    "http.url": "http://example.com",
    "my.custom.application.tag": "hello"
  },
  "resource": {
    "service.name": "donut_shop",
    "service.version": "semver:2.0.0",
    "k8s.pod.name": "1138528c-c36e-11e9-a1a7-42010a800198"
  },
  "trace_id": "f4dbb3edd765f620",
  "span_id": "43222c2d51a7abe3",
  "severity": "INFO",
  "body": {
    "i": "am",
    "an": "event",
    "of": {
      "some": "complexity"
    }
  }
}
```

## Usage

```
pip install --upgrade linz-logger
```

```python
from os import environ

from linz_logger import get_log, set_level, LogLevel

set_level(LogLevel[environ.get("LOGLEVEL", "WARNING").lower()].value)
set_contextvars({"country": "NZ"}) # remove_contextvars(["country"]) to remove a key
get_log().error('Hello World', key="value")
# {"key": "value", "level": 50, "time": 1601555605017, "v": 1, "pid": 311800, "id": "01G9XAA1MCMX2K9NZN9GJJHN71", "msg": "Hello World", "hostname": "Ubuntu1", "country": "NZ"}
```
