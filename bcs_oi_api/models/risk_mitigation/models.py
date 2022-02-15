from bcs_oi_api.models.models import BCSOIAPIBaseModel


__all__ = [
    'RiskMitigationDetails', 'RiskMitigationSummary'
]


class RiskMitigationDetails(BCSOIAPIBaseModel):
    device_id: int
    device_ip: str
    device_name: str
    product_family: str
    product_id: str
    risk_category: str
    risk_score: float
    software_type: str
    software_version: str

    @classmethod
    def url_path(cls):
        return 'riskMitigation/details'
    

class RiskMitigationSummary(BCSOIAPIBaseModel):
    high_risk_device_count: int
    low_risk_device_count: int
    medium_risk_device_count: int
    product_family: str

    @classmethod
    def url_path(cls):
        return 'riskMitigation/summary'