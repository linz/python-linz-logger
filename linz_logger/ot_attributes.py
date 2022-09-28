from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class OpenTelemetryAttributes:
    """https://github.com/open-telemetry/oteps/blob/main/text/logs/0097-log-data-model.md#field-attributes"""

    error_id: Optional[str] = field(metadata=config(field_name="error.id"), default=None)
    error_code: Optional[str] = field(metadata=config(field_name="error.code"), default=None)
    error_message: Optional[str] = field(metadata=config(field_name="error.message"), default=None)
    error_stack_trace: Optional[str] = field(metadata=config(field_name="error.stack_trace"), default=None)
