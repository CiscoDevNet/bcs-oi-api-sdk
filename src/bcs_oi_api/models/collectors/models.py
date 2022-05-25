from datetime import datetime
from typing import Optional

from ..models import BCSOIAPIBaseModel

__all__ = ["Collector"]


class Collector(BCSOIAPIBaseModel):
    appliance_id: str
    collector_name: str
    collector_status: str
    collector_version: str
    expected_upload_interval: int
    last_upload_timestamp: Optional[datetime]

    @classmethod
    def url_path(cls) -> str:
        return "collectors"
