from typing import Optional

from ..models import BCSOIAPIBaseModel

__all__ = ["RiskMitigationDetails", "RiskMitigationSummary"]


class RiskMitigationDetails(BCSOIAPIBaseModel):
    device_id: int
    device_ip: str
    device_name: str
    product_family: str
    product_id: Optional[str]  # Optional for bulk
    risk_category: str
    risk_score: float
    software_type: str
    software_version: str

    @classmethod
    def url_path(cls) -> str:
        return "riskMitigation/details"


class RiskMitigationSummary(BCSOIAPIBaseModel):
    high_risk_device_count: int
    low_risk_device_count: int
    medium_risk_device_count: int
    product_family: str

    @classmethod
    def url_path(cls) -> str:
        return "riskMitigation/summary"
