from datetime import datetime

from src.bcs_oi_api.models import LastResetDetails, ResetCount, ResetHistory
from tests.utils import check_model_creation

reset_count_1 = {"devicesCrashCount": 4, "devicesReloadCount": 0}

reset_history_1 = {
    "deviceId": 5091900,
    "deviceIp": "10.80.77.254",
    "deviceName": "MY-KUL-SPP-L35-RTR01",
    "productFamily": "Cisco 4000 Series Integrated Services Routers",
    "productId": "ISR4431/K9",
    "resetDetails": [
        {
            "resetTimestamp": "2021-08-21T10:58:44",
            "resetReason": "Critical software exception, check bootflash:crashinfo_RP_00_00_20210821-085029-UTC",
            "resetType": "crash",
            "softwareType": "IOS-XE",
            "softwareVersion": "16.8.3",
        },
        {
            "resetTimestamp": "2021-11-29T09:38:08",
            "resetReason": "Critical software exception, check bootflash:crashinfo_RP_00_00_20211129-083227-UTC",
            "resetType": "crash",
            "softwareType": "IOS-XE",
            "softwareVersion": "16.8.3",
        },
    ],
}

last_reset_details_1 = {
    "deviceId": 4761645,
    "deviceIp": "10.39.236.65",
    "deviceName": "BHPCLPAGSW01",
    "inventoryTimestamp": "2021-12-02T17:20:09",
    "lastResetTimestamp": "2021-09-27T21:57:27",
    "productFamily": "Cisco Catalyst 3850 Series Switches",
    "productId": "WS-C3850-24P-S",
    "resetReason": "Power Failure or Unknown",
    "resetType": "reload",
    "softwareType": "IOS-XE",
    "softwareVersion": "16.6.4a",
}

last_reset_details_2 = {
    "deviceId": 4761645,
    "deviceIp": "10.39.236.65",
    "deviceName": "BHPCLPAGSW01",
    "inventoryTimestamp": None,
    "lastResetTimestamp": "2021-09-27T21:57:27",
    "productFamily": "Cisco Catalyst 3850 Series Switches",
    "productId": "WS-C3850-24P-S",
    "resetReason": "Power Failure or Unknown",
    "resetType": "reload",
    "softwareType": "IOS-XE",
    "softwareVersion": "16.6.4a",
}


def test_reset_count_model() -> None:
    reset_count = ResetCount(**reset_count_1)
    check_model_creation(input_dict=reset_count_1, model_instance=reset_count)


def test_reset_history_model() -> None:
    reset_history = ResetHistory(**reset_history_1)
    check_model_creation(input_dict=reset_history_1, model_instance=reset_history)


def test_last_reset_details_model() -> None:
    for last_reset_details_dict in [last_reset_details_1, last_reset_details_2]:
        last_reset_details = LastResetDetails(**last_reset_details_dict)
        check_model_creation(input_dict=last_reset_details_dict, model_instance=last_reset_details)
