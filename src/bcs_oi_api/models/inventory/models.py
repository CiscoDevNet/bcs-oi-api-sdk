from datetime import datetime
from typing import Optional

from ..models import BCSOIAPIBaseModel

__all__ = ["Asset", "Device"]


class Device(BCSOIAPIBaseModel):
    collector_name: str
    config_register: str
    config_status: str
    config_timestamp: Optional[datetime]
    created_timestamp: Optional[datetime]
    device_id: int
    device_ip: str
    device_name: str
    device_status: str
    device_type: str
    feature_set_description: str
    image_name: str
    inventory_status: str
    inventory_timestamp: Optional[datetime]
    ip_address: str
    is_in_seed_file: bool
    last_reset_timestamp: Optional[datetime]
    product_family: str
    product_id: str
    product_type: str
    reset_reason: str
    snmp_sys_contact: str
    snmp_sys_description: str
    snmp_sys_location: str
    snmp_sys_name: str
    snmp_sys_object_id: str
    software_type: str
    software_version: str
    user_field_1: str
    user_field_2: str
    user_field_3: str
    user_field_4: str

    @classmethod
    def url_path(cls) -> str:
        return "inventory/devices"


class Asset(BCSOIAPIBaseModel):
    chassis_name: str
    device_id: int
    device_name: str
    hardware_revision: str
    installed_flash: Optional[int]
    installed_memory: Optional[int]
    printed_circuit_board_name: str
    printed_circuit_board_revision: str
    physical_asset_id: int
    physical_asset_subtype: str
    physical_asset_type: str
    product_family: str
    product_id: str
    product_type: str
    serial_number: str
    serial_number_status: str
    slot: str
    software_version: str
    top_assembly_number: str
    top_assembly_number_revision: str

    @classmethod
    def url_path(cls) -> str:
        return "inventory/assets"
