from src.bcs_oi_api.models import RiskMitigationDetails, RiskMitigationSummary
from tests.utils import check_model_creation

risk_mitigation_detail_1 = {
    "deviceId": 5848341,
    "deviceIp": "10.41.89.252",
    "deviceName": "msglb01",
    "productFamily": "Cisco Catalyst 6500 Series Switches",
    "productId": "WS-C6509-E",
    "riskCategory": "High",
    "riskScore": 30.26,
    "softwareType": "IOS",
    "softwareVersion": "15.1(2)SY12",
}


def test_risk_mitigation_detail_model() -> None:
    risk_mitigation_detail = RiskMitigationDetails(**risk_mitigation_detail_1)
    check_model_creation(input_dict=risk_mitigation_detail_1, model_instance=risk_mitigation_detail)


risk_mitigation_summary_1 = {
    "highRiskDeviceCount": 0,
    "lowRiskDeviceCount": 28,
    "mediumRiskDeviceCount": 56,
    "productFamily": "Cisco Nexus 5000 Series Switches",
}


def test_risk_mitigation_summary_model() -> None:
    risk_mitigation_summary = RiskMitigationSummary(**risk_mitigation_summary_1)
    check_model_creation(input_dict=risk_mitigation_summary_1, model_instance=risk_mitigation_summary)
