import os

import pytest

from src.bcs_oi_api.bcs_oi_api import BCSOIAPI
from src.bcs_oi_api.models import Device, DeviceFilter, UIRSummary


def test_lib_base_inventory_devices() -> None:
    client_id = os.getenv("SDK_TEST_CLIENT_ID")
    client_secret = os.getenv("SDK_TEST_CLIENT_SECRET")

    assert client_id is not None, "Test client id not set in environment"
    assert client_secret is not None, "Test client secret not set in environment"

    bcs_oi_api = BCSOIAPI(client_id=client_id, client_secret=client_secret, region="us")

    devices = bcs_oi_api.get_output(model=Device)
    devices_dict = {device.device_id: device for device in devices}

    assert devices_dict != {}


def test_lib_filter_inventory_devices() -> None:
    client_id = os.getenv("SDK_TEST_CLIENT_ID")
    client_secret = os.getenv("SDK_TEST_CLIENT_SECRET")

    assert client_id is not None, "Test client id not set in environment"
    assert client_secret is not None, "Test client secret not set in environment"

    bcs_oi_api = BCSOIAPI(client_id=client_id, client_secret=client_secret, region="us")

    filter_ = DeviceFilter(device_id=[24932787, 24932788], inventory_status=["NotAvailable"])

    devices = bcs_oi_api.get_output(model=Device, filter_=filter_)
    devices_dict = {device.device_id: device for device in devices}

    assert len(devices_dict) == 2


def test_lib_fields_inventory_devices() -> None:
    client_id = os.getenv("SDK_TEST_CLIENT_ID")
    client_secret = os.getenv("SDK_TEST_CLIENT_SECRET")

    assert client_id is not None, "Test client id not set in environment"
    assert client_secret is not None, "Test client secret not set in environment"

    bcs_oi_api = BCSOIAPI(client_id=client_id, client_secret=client_secret, region="us")

    devices = bcs_oi_api.get_output(model=Device, fields="deviceId")
    devices_dict = {device.device_id: device for device in devices}

    assert devices_dict != {}


def test_lib_wrong_fields_inventory_devices() -> None:
    client_id = os.getenv("SDK_TEST_CLIENT_ID")
    client_secret = os.getenv("SDK_TEST_CLIENT_SECRET")

    assert client_id is not None, "Test client id not set in environment"
    assert client_secret is not None, "Test client secret not set in environment"

    bcs_oi_api = BCSOIAPI(client_id=client_id, client_secret=client_secret, region="us")

    devices = bcs_oi_api.get_output(model=Device, fields="deviceId")
    with pytest.raises(AttributeError):
        _ = {device.collector_name: device for device in devices}


def test_lib_filter_fields_inventory_devices() -> None:
    client_id = os.getenv("SDK_TEST_CLIENT_ID")
    client_secret = os.getenv("SDK_TEST_CLIENT_SECRET")

    assert client_id is not None, "Test client id not set in environment"
    assert client_secret is not None, "Test client secret not set in environment"

    bcs_oi_api = BCSOIAPI(client_id=client_id, client_secret=client_secret, region="us")

    filter_ = DeviceFilter(device_id=[24932787, 24932788], inventory_status=["NotAvailable"])

    devices = bcs_oi_api.get_output(model=Device, filter_=filter_, fields="deviceId")
    devices_dict = {device.device_id: device for device in devices}

    assert len(devices_dict) == 2


def test_uir_summary() -> None:
    client_id = os.getenv("SDK_TEST_CLIENT_ID")
    client_secret = os.getenv("SDK_TEST_CLIENT_SECRET")

    assert client_id is not None, "Test client id not set in environment"
    assert client_secret is not None, "Test client secret not set in environment"

    bcs_oi_api = BCSOIAPI(client_id=client_id, client_secret=client_secret, region="us")

    uir_summary = bcs_oi_api.get_output(model=UIRSummary)
    uir_summary_dict = next(uir_summary).dict()

    assert uir_summary_dict != {}

    fields = "unidentifiedDeviceCount"
    uir_summary = bcs_oi_api.get_output(model=UIRSummary, fields=fields)
    assert next(uir_summary).unidentified_device_count is not None
