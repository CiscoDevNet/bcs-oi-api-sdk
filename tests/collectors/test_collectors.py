from src.bcs_oi_api.models import Collector
from tests.utils import check_model_creation

collector_1 = {
    "applianceId": "CSP0009031587",
    "collectorName": "bci2",
    "collectorStatus": "Cisco Testing",
    "collectorVersion": "2.8.1.8",
    "expectedUploadInterval": 8,
    "lastUploadTimestamp": "2022-02-03T21:10:58",
}

collector_2 = {
    "applianceId": "CSP0009031587",
    "collectorName": "bci2",
    "collectorStatus": "Cisco Testing",
    "collectorVersion": "2.8.1.8",
    "expectedUploadInterval": 8,
    "lastUploadTimestamp": None,
}


def test_collector_model():
    for collector_dict in [collector_1, collector_2]:
        collector = Collector(**collector_dict)
        check_model_creation(input_dict=collector_dict, model_instance=collector)
