from dataclasses import dataclass, field

from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class OpenTelemetryResourceHost:
    """_summary_"""

    host_name: str = field(metadata=config(field_name="host.name"), default="")
    host_id: str = field(metadata=config(field_name="host.id"), default="")
    host_ip: str = field(metadata=config(field_name="host.ip"), default="")
    host_mac: str = field(metadata=config(field_name="host.mac"), default="")
