from dataclasses import dataclass, field

from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class OpenTelemetryAttributes:
    """_summary_"""

    error_id: str = field(metadata=config(field_name="error.id"), default="")
    error_code: str = field(metadata=config(field_name="error.code"), default="")
    error_message: str = field(metadata=config(field_name="error.message"), default="")
    error_stack_trace: str = field(metadata=config(field_name="error.stack_trace"), default="")
