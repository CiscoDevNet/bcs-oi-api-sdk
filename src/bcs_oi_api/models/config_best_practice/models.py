from datetime import datetime
from typing import Optional

from ..models import BCSOIAPIBaseModel

__all__ = [
    "ConfigBestPracticeRule",
    "ConfigBestPracticeRuleReference",
    "ConfigBestPracticeDetail",
    "ConfigBestPracticeSummary",
]


class ConfigBestPracticeRule(BCSOIAPIBaseModel):
    best_practice_caveat: str
    best_practice_corrective_action: str
    best_practice_description: str
    best_practice_nugget_id: int
    best_practice_primary_technology: str
    best_practice_recommendation: str
    best_practice_risk: str
    best_practice_rule_id: int
    best_practice_secondary_technology: str
    best_practice_title: str
    created_timestamp: Optional[datetime]
    software_type: str
    best_practice_rule_modification_timestamp: Optional[datetime]

    @classmethod
    def url_path(cls) -> str:
        return "configBestPractices/rules"


class ConfigBestPracticeRuleReference(BCSOIAPIBaseModel):
    best_practice_rule_id: int
    best_practice_url: str
    best_practice_url_title: str

    @classmethod
    def url_path(cls) -> str:
        return "configBestPractices/rulesReferences"


class ConfigBestPracticeSummary(BCSOIAPIBaseModel):
    best_practice_nugget_id: int
    best_practice_primary_technology: str
    best_practice_risk: str
    best_practice_rule_id: int
    best_practice_secondary_technology: str
    best_practice_title: str
    software_type: str
    total_device_count: int

    @classmethod
    def url_path(cls) -> str:
        return "configBestPractices/summary"


class ConfigBestPracticeDetail(BCSOIAPIBaseModel):
    best_practice_nugget_id: int
    best_practice_rule_id: int
    config_source: str
    device_id: Optional[int]  # Optional for bulk

    @classmethod
    def url_path(cls) -> str:
        return "configBestPractices/details"
