from src.bcs_oi_api.models import Asset, Device
from tests.utils import check_model_creation

asset_1: dict = {
    "chassisName": "10.201.23.147",
    "deviceId": 24948009,
    "deviceName": "10.201.23.147",
    "hardwareRevision": "",
    "installedFlash": None,
    "installedMemory": None,
    "printedCircuitBoardName": "",
    "printedCircuitBoardRevision": "",
    "physicalAssetId": 477944695,
    "physicalAssetSubtype": "",
    "physicalAssetType": "Fan",
    "productFamily": "Catalyst 2K/3K Series Fans",
    "productId": "FAN-T1=",
    "productType": "Fans",
    "serialNumber": "",
    "serialNumberStatus": "N/A",
    "slot": "FAN1",
    "softwareVersion": "",
    "topAssemblyNumber": "",
    "topAssemblyNumberRevision": "",
}

asset_2: dict = {
    "chassisName": "10.201.23.147",
    "deviceId": 24948009,
    "deviceName": "10.201.23.147",
    "hardwareRevision": "",
    "installedFlash": 2048,
    "installedMemory": 1024,
    "printedCircuitBoardName": "",
    "printedCircuitBoardRevision": "",
    "physicalAssetId": 477944695,
    "physicalAssetSubtype": "",
    "physicalAssetType": "Fan",
    "productFamily": "Catalyst 2K/3K Series Fans",
    "productId": "FAN-T1=",
    "productType": "Fans",
    "serialNumber": "",
    "serialNumberStatus": "N/A",
    "slot": "FAN1",
    "softwareVersion": "",
    "topAssemblyNumber": "",
    "topAssemblyNumberRevision": "",
}


def test_asset_model() -> None:
    for asset_dict in [asset_1, asset_2]:
        asset = Asset(**asset_dict)
        check_model_creation(input_dict=asset_dict, model_instance=asset)


device_1: dict = {
    "collectorName": "mycollector",
    "configRegister": "2102",
    "configStatus": "Completed",
    "configTimestamp": "2022-02-02T15:33:37",
    "createdTimestamp": "2022-02-02T15:33:37",
    "deviceId": 22345640,
    "deviceIp": "172.21.1.1",
    "deviceName": "switch",
    "deviceStatus": "ACTIVE",
    "deviceType": "Unmanaged Chassis",
    "featureSetDescription": "",
    "imageName": "",
    "inventoryStatus": "Completed",
    "inventoryTimestamp": "2022-02-02T15:33:37",
    "ipAddress": "172.16.1.1",
    "isInSeedFile": True,
    "lastResetTimestamp": "2022-02-02T15:33:37",
    "productFamily": "Cisco Catalyst 3560-E Series Switches",
    "productId": "WS-C3560X-24P-E",
    "productType": "Metro Ethernet Switches",
    "resetReason": "",
    "snmpSysContact": "",
    "snmpSysDescription": "",
    "snmpSysLocation": "",
    "snmpSysName": "",
    "snmpSysObjectId": "",
    "softwareType": "IOS",
    "softwareVersion": "15.1(4)M4",
    "userField1": "",
    "userField2": "",
    "userField3": "",
    "userField4": "",
}


device_2: dict = {
    "collectorName": "mycollector",
    "configRegister": "2102",
    "configStatus": "Completed",
    "configTimestamp": None,
    "createdTimestamp": None,
    "deviceId": 22345640,
    "deviceIp": "172.21.1.1",
    "deviceName": "switch",
    "deviceStatus": "ACTIVE",
    "deviceType": "Unmanaged Chassis",
    "featureSetDescription": "",
    "imageName": "",
    "inventoryStatus": "Completed",
    "inventoryTimestamp": None,
    "ipAddress": "172.16.1.1",
    "isInSeedFile": True,
    "lastResetTimestamp": None,
    "productFamily": "Cisco Catalyst 3560-E Series Switches",
    "productId": "WS-C3560X-24P-E",
    "productType": "Metro Ethernet Switches",
    "resetReason": "",
    "snmpSysContact": "",
    "snmpSysDescription": "",
    "snmpSysLocation": "",
    "snmpSysName": "",
    "snmpSysObjectId": "",
    "softwareType": "IOS",
    "softwareVersion": "15.1(4)M4",
    "userField1": "",
    "userField2": "",
    "userField3": "",
    "userField4": "",
}


def test_device_model() -> None:
    for device_dict in [device_1, device_2]:
        device = Device(**device_dict)
        check_model_creation(input_dict=device_dict, model_instance=device)
