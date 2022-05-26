from src.bcs_oi_api.models.place_in_network import PINDetails
from tests.utils import check_model_creation

details_1 = {"deviceId": 22345640, "deviceName": "router%", "predictedImportance": "Medium", "predictedRole": "Core"}


def test_place_in_network_details_model() -> None:
    details = PINDetails(**details_1)
    check_model_creation(input_dict=details_1, model_instance=details)
