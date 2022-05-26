from src.bcs_oi_api.models import DeviceGroup, DeviceGroupMember
from tests.utils import check_model_creation

device_group_member_1 = {"deviceId": 24932787, "groupId": 366841, "groupName": "bci2"}

device_group_1 = {
    "groupDescription": "Test lab 2 for BCS",
    "groupId": 366841,
    "groupName": "bci2",
    "groupTotalDeviceCount": 2,
}


def test_device_group_member_model() -> None:
    device_group_member = DeviceGroupMember(**device_group_member_1)
    check_model_creation(input_dict=device_group_member_1, model_instance=device_group_member)


def test_device_group_model() -> None:
    device_group = DeviceGroup(**device_group_1)
    check_model_creation(input_dict=device_group_1, model_instance=device_group)
