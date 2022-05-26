from src.bcs_oi_api.models.unidentified_inventory import UIRDetails, UIRSummary
from tests.utils import check_model_creation

details_1 = {
    "unidentifiedDeviceName": "N5K-4",
    "unidentifiedDeviceIpAddress": "10.201.23.128",
    "unidentifiedDeviceSource": " CDP",
    "seenByManagedDeviceName": "10.1.27.250",
    "collectorName": "bcs1",
    "unidentifiedDeviceStatus": "Recurring",
    "unidentifiedDevicePlatform": "N9K-C9372PX",
    "unidentifiedDeviceScore": 1,
    "lastUpdatedTimestamp": "2022-02-14T19:57:18",
}


def test_unidentified_inventory_details_model() -> None:
    details = UIRDetails(**details_1)
    check_model_creation(input_dict=details_1, model_instance=details)


summary_1 = {
    "unidentifiedDeviceCount": 295,
    "newUnidentifiedDeviceCount": 52,
    "recurringUnidentifiedDeviceCount": 243,
    "newlyManagedUnidentifiedDeviceCount": 25,
    "deletedUnidentifiedDeviceCount": 29,
    "cdpSourcedUnidentifiedDeviceCount": 270,
    "syslogSourcedUnidentifiedDeviceCount": 1,
    "configSubnetSourcedUnidentifiedDeviceCount": 24,
    "configProtocolSourcedUnidentifiedDeviceCount": 0,
    "lastUpdatedTimestamp": "2022-02-14T19:57:18",
}


def test_unidentified_inventory_summary_model() -> None:
    summary = UIRSummary(**summary_1)
    check_model_creation(input_dict=summary_1, model_instance=summary)
