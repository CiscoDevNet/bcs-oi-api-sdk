from src.bcs_oi_api.models import Syslog
from tests.utils import check_model_creation

syslog_1 = {
    "date": "2021-08-02",
    "description": "The specified PM TCA has been declared.",
    "devices": [
        {"deviceName": "10.89.200.203", "deviceId": 26364428, "eventCount": 194},
        {"deviceName": "10.89.200.206", "deviceId": None, "eventCount": 97},
    ],
    "messageType": "L1-PMENGINE-4-TCA",
    "totalEventCount": 291,
    "recommendation": "It is recommended to repair the source of the alarm.",
    "reviewedSeverity": 4,
    "syslogEventSeverity": 4,
    "timestamp": "2021-08-02T00:00:00",
}


def test_syslog_model():
    syslog = Syslog(**syslog_1)
    check_model_creation(input_dict=syslog_1, model_instance=syslog)
