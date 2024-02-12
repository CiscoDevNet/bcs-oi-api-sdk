from typing import List, Optional

from ..models import BCSOIAPIBaseModel

__all__ = ["SIDetails", "SISummary", "SIRuleDetails", "SIDetailsFilter", "SIRuleDetailsFilter"]


class SIDetails(BCSOIAPIBaseModel):
    device_id: str
    rule_id: str
    scalability_percent: float
    scalability_value: int

    @classmethod
    def url_path(cls) -> str:
        return "scalabilityInsights/details"


class SISummary(BCSOIAPIBaseModel):
    device_count: int
    rule_id: str
    rule_name: str

    @classmethod
    def url_path(cls) -> str:
        return "scalabilityInsights/summary"


class SIRuleDetails(BCSOIAPIBaseModel):
    rule_category: str
    rule_id: str
    rule_name: str
    rule_sub_category: str
    scalability_limit: int

    @classmethod
    def url_path(cls) -> str:
        return "scalabilityInsights/rulesDetails"


class SIDetailsFilter(BCSOIAPIBaseModel):
    threshold: Optional[List[float]]


class SIRuleDetailsFilter(BCSOIAPIBaseModel):
    rule_id: Optional[List[str]]
