from src.bcs_oi_api.models import Collector

collector_1 = {
    "applianceId": "CSP0009031587",
    "collectorName": "bci2",
    "collectorStatus": "Cisco Testing",
    "collectorVersion": "2.8.1.8",
    "expectedUploadInterval": 8,
    "lastUploadTimestamp": "2022-02-03T21:10:58",
}


def test_collector_model() -> None:
    collector = Collector(**collector_1)
    assert collector.appliance_id == collector_1["applianceId"]
