from datetime import datetime
from typing import List, Optional

from ..models import BCSOIAPIBaseModel

__all__ = ["LastResetDetails", "ResetCount", "ResetHistory"]


class LastResetDetails(BCSOIAPIBaseModel):
    device_id: int
    device_ip: str
    device_name: str
    inventory_timestamp: Optional[datetime]
    last_reset_timestamp: datetime
    product_family: str
    product_id: str
    reset_reason: str
    reset_type: str
    software_type: str
    software_version: str

    @classmethod
    def url_path(cls) -> str:
        return "deviceReset/lastResetDetails"


class ResetCount(BCSOIAPIBaseModel):
    devices_crash_count: int
    devices_reload_count: int

    @classmethod
    def url_path(cls) -> str:
        return "deviceReset/resetCount"

    @classmethod
    def response_items(cls) -> bool:
        return False


class ResetDetails(BCSOIAPIBaseModel):
    reset_timestamp: datetime
    reset_reason: str
    reset_type: str
    software_type: str
    software_version: str


class ResetHistory(BCSOIAPIBaseModel):
    device_id: int
    device_ip: str
    device_name: str
    product_family: str
    product_id: str
    reset_details: List[ResetDetails]

    @classmethod
    def url_path(cls) -> str:
        return "deviceReset/resetHistory"
