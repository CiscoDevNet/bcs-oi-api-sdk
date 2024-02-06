from src.bcs_oi_api.models.policy_variation_analysis import PvaDetails, PvaPolicies, PvaVariations
from tests.utils import check_model_creation

policy_1 = {
    "applied": 1,
    "appliedInterfaces": [{"direction": "in", "interface": "snmp"}],
    "deviceId": "24932787",
    "similarityHash": "28b10525e413de37c2654508fb25d669",
    "hostName": "DC-Fanout-1-P2",
    "policyName": "nexus-10",
    "policyType": "acl",
    "productFamily": "Missing",
    "subPolicyType": "STANDARD",
}


def test_pva_devices_policies_model() -> None:
    policies = PvaPolicies(**policy_1)
    check_model_creation(input_dict=policy_1, model_instance=policies)


details_1 = {
    "applied": 1,
    "deviceCount": 1,
    "policyComplexity": "Medium",
    "policyName": "BFD",
    "policyType": "class-map",
    "productFamily": "Cisco ASR 9000 Series Aggregation Services Routers",
    "subPolicyType": "SSID",
    "policyVariations": 2,
}


def test_pva_details_model() -> None:
    details = PvaDetails(**details_1)
    check_model_creation(input_dict=details_1, model_instance=details)


policy_variations_1 = {
    "isPrimaryPolicyVariation": "true",
    "deviceCount": 3,
    "similarityHash": "44e2d8127c6d7d0b10ecfe2733d6243d",
    "policyName": "SSM_RANGE_HTTS",
    "policyType": "acl",
    "productFamily": "Cisco ASR 9000 Series Aggregation Services Routers",
    "subPolicyType": "IOS-XR",
}


def test_pva_variations_model() -> None:
    variations = PvaVariations(**policy_variations_1)
    check_model_creation(input_dict=policy_variations_1, model_instance=variations)
