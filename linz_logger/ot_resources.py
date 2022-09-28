from dataclasses import dataclass, field

from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class OpenTelemetryResource:
    """https://github.com/open-telemetry/oteps/blob/main/text/logs/0097-log-data-model.md#field-resource"""

    host_name: str = field(metadata=config(field_name="host.name"), default="")
    host_id: str = field(metadata=config(field_name="host.id"), default="")
    host_ip: str = field(metadata=config(field_name="host.ip"), default="")
    host_mac: str = field(metadata=config(field_name="host.mac"), default="")

    container_id: str = field(metadata=config(field_name="container.id"), default="")
    container_image_name: str = field(metadata=config(field_name="container.image.name"), default="")
    container_image_hash: str = field(metadata=config(field_name="container.image.hash"), default="")
    container_name: str = field(metadata=config(field_name="container.name"), default="")
