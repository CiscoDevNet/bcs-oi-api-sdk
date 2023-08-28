from typing import List, Optional

from ..models import BCSOIAPIBaseModel

__all__ = ["SIDetails", "SISummary","SISummaryFilter","SIDetailsFilter"]


class SIDetails(BCSOIAPIBaseModel):
    device_id: str
    rule_id: str
    scalability_percent: float
    scalability_value: int

    @classmethod
    def url_path(cls) -> str:
        return "scalabilityInsights/device-details"


class SISummary(BCSOIAPIBaseModel):
    device_count: int
    rule_id: str
    rule_name: str

    @classmethod
    def url_path(cls) -> str:
        return "scalabilityInsights/device-summary"


class SIDetailsFilter(BCSOIAPIBaseModel):
    threshold: Optional[List[int]]


class SISummaryFilter(BCSOIAPIBaseModel):
    threshold : Optional[List[int]]
