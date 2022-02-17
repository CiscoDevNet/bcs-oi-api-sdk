from ..models import BCSOIAPIBaseModel

__all__ = ["DeviceGroup", "DeviceGroupMember"]


class DeviceGroupMember(BCSOIAPIBaseModel):
    device_id: int
    group_id: int
    group_name: str

    @classmethod
    def url_path(cls) -> str:
        return "deviceGroups/groupMembers"


class DeviceGroup(BCSOIAPIBaseModel):
    group_description: str
    group_id: int
    group_name: str
    group_total_device_count: int

    @classmethod
    def url_path(cls) -> str:
        return "deviceGroups/groups"
