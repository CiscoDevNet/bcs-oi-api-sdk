from src.bcs_oi_api.models import DeviceGroup, DeviceGroupMember

device_group_member_1 = {"deviceId": 24932787, "groupId": 366841, "groupName": "bci2"}

device_group_1 = {
    "groupDescription": "Test lab 2 for BCS",
    "groupId": 366841,
    "groupName": "bci2",
    "groupTotalDeviceCount": 2,
}


def test_device_group_member_model():
    device_group_member = DeviceGroupMember(**device_group_member_1)
    assert device_group_member.group_id == device_group_member_1["groupId"]


def test_device_group_model():
    device_group = DeviceGroup(**device_group_1)
    assert device_group.group_id == device_group_1["groupId"]
