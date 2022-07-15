from datetime import datetime
from typing import Optional

from ..models import BCSOIAPIBaseModel

__all__ = ["UIRDetails", "UIRSummary"]


class UIRDetails(BCSOIAPIBaseModel):
    collector_name: str
    unidentified_device_name: str
    unidentified_device_ip_address: str
    unidentified_device_source: str
    unidentified_device_status: str
    unidentified_device_platform: str
    unidentified_device_score: int
    seen_by_managed_device_name: str
    last_updated_timestamp: datetime

    @classmethod
    def url_path(cls) -> str:
        return "unidentifiedInventory/details"


class UIRSummary(BCSOIAPIBaseModel):
    unidentified_device_count: int
    new_unidentified_device_count: int
    recurring_unidentified_device_count: int
    newly_managed_unidentified_device_count: int
    deleted_unidentified_device_count: int
    cdp_sourced_unidentified_device_count: int
    syslog_sourced_unidentified_device_count: int
    config_subnet_sourced_unidentified_device_count: int
    config_protocol_sourced_unidentified_device_count: int
    last_updated_timestamp: datetime

    @classmethod
    def url_path(cls) -> str:
        return "unidentifiedInventory/summary"

    @classmethod
    def response_items(cls) -> bool:
        return False


class UIRDetailsFilter(BCSOIAPIBaseModel):
    unidentified_device_name: Optional[list]
    unidentified_device_status: Optional[list]
