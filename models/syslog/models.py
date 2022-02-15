from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from bcs_oi_api.models.models import BCSOIAPIBaseModel

__all__ = ["Syslog"]


class SyslogDevice(BCSOIAPIBaseModel):
    device_name: str
    device_id: Optional[int]
    event_count: int


class Syslog(BCSOIAPIBaseModel):
    date: date
    description: str
    devices: List[SyslogDevice]
    message_type: str
    total_event_count: int
    recommendation: str
    reviewed_severity: int
    syslog_event_severity: int
    timestamp: datetime

    @classmethod
    def url_path(cls):
        return "syslog/daily"
