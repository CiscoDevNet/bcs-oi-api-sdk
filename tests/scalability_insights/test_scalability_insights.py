from src.bcs_oi_api.models.scalability_insights import SIDetails, SISummary
from tests.utils import check_model_creation

details_1 = {
    "deviceId": "28564936",
    "ruleId": "782cddb9f7_e751da28a4_a5236bb145_b9077e4b6e_4b18ec6f4c_8a6f5101c5",
    "scalabilityPercent": 0.02,
    "scalabilityValue": 2
}


def test_unidentified_inventory_details_model() -> None:
    details = SIDetails(**details_1)
    check_model_creation(input_dict=details_1, model_instance=details)


summary_1 = {
    "deviceCount": 12,
    "ruleId": "782cddb9f7_b1f7f66331_a5236bb145_b9077e4b6e_4b18ec6f4c_e19172620f",
    "ruleName": "BGP Routes"
}


def test_unidentified_inventory_summary_model() -> None:
    summary = SISummary(**summary_1)
    check_model_creation(input_dict=summary_1, model_instance=summary)
