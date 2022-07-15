from datetime import datetime
from typing import Optional
<<<<<<< HEAD
=======

>>>>>>> master
from ..models import BCSOIAPIBaseModel

__all__ = ["Collector"]


class Collector(BCSOIAPIBaseModel):
    appliance_id: str
    collector_name: str
    collector_status: str
    collector_version: str
    expected_upload_interval: int
<<<<<<< HEAD
    last_upload_timestamp: datetime
=======
    last_upload_timestamp: Optional[datetime]
>>>>>>> master

    @classmethod
    def url_path(cls) -> str:
        return "collectors"
<<<<<<< HEAD


class CollectorFilter(BCSOIAPIBaseModel):
    appliance_id: Optional[list]
    collector_status: Optional[list]
=======
>>>>>>> master
