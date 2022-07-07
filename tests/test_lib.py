import os
from src.bcs_oi_api.bcs_oi_api import BCSOIAPI
from src.bcs_oi_api.models import Device


def test_lib_base() -> None:
    client_id = os.getenv("SDK_TEST_CLIENT_ID")
    client_secret = os.getenv("SDK_TEST_CLIENT_SECRET")

    assert client_id is not None, "Test client id not set in environment"
    assert client_secret is not None, "Test client secret not set in environment"

    bcs_oi_api = BCSOIAPI(client_id=client_id, client_secret=client_secret, region="us")

    devices = bcs_oi_api.get_output(model=Device)
    devices_dict = {device.device_id: device for device in devices}

    assert devices_dict != {}
