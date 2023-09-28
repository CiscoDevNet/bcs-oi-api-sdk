from src.bcs_oi_api.models import (
    ConfigBestPracticeDetail,
    ConfigBestPracticeRule,
    ConfigBestPracticeRuleReference,
    ConfigBestPracticeSummary,
)
from tests.utils import check_model_creation

config_best_practice_rule_1 = {
    "bestPracticeCaveat": "",
    "bestPracticeCorrectiveAction": "In the global configuration mode,enter 'snmp-server enable traps system' "
    "command to enable system traps.",
    "bestPracticeDescription": "If NX-OS device has system configured and running and SNMP Traps enabled then flag an "
    "exception if globally you don't find:  \n\nsnmp-server enable traps system",
    "bestPracticeNuggetId": "IOS_XR_UNSUPP_TRANSEIVER",
    "bestPracticePrimaryTechnology": "*Network Management",
    "bestPracticeRecommendation": "Cisco recommends to enable SNMP traps,as they are helpful to log the event "
    "related to system process and can be used for troubleshooting when required.",
    "bestPracticeRisk": "Low",
    "bestPracticeRuleId": "11148",
    "bestPracticeSecondaryTechnology": "",
    "bestPracticeTitle": "System SNMP Traps Not Enabled",
    "createdTimestamp": "2016-06-04T04:01:00",
    "softwareType": "NX-OS",
    "bestPracticeRuleModificationTimestamp": "2021-06-04T04:01:00",
}

config_best_practice_rule_2 = {
    "bestPracticeCaveat": "",
    "bestPracticeCorrectiveAction": "In the global configuration mode,enter 'snmp-server enable traps system' "
    "command to enable system traps.",
    "bestPracticeDescription": "If NX-OS device has system configured and running and SNMP Traps enabled then flag an "
    "exception if globally you don't find:  \n\nsnmp-server enable traps system",
    "bestPracticeNuggetId": "IOS_XR_UNSUPP_TRANSEIVER",
    "bestPracticePrimaryTechnology": "*Network Management",
    "bestPracticeRecommendation": "Cisco recommends to enable SNMP traps,as they are helpful to log the event "
    "related to system process and can be used for troubleshooting when required.",
    "bestPracticeRisk": "Low",
    "bestPracticeRuleId": "11148",
    "bestPracticeSecondaryTechnology": "",
    "bestPracticeTitle": "System SNMP Traps Not Enabled",
    "createdTimestamp": None,
    "softwareType": "NX-OS",
    "bestPracticeRuleModificationTimestamp": None,
}


config_best_practice_rule_reference_1 = {
    "bestPracticeRuleId": "11148",
    "bestPracticeUrl": "http://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus7000/sw/system-management/"
    "command/reference/n7k_sm_cmd_ref/sm_cmd_s.html#pgfId-1035395",
    "bestPracticeUrlTitle": "Nexus 7000 System Command Reference",
}

config_best_practice_detail_1 = {
    "bestPracticeNuggetId": "IOS_XR_UNSUPP_TRANSEIVER",
    "bestPracticeRuleId": "11148",
    "configSource": "STANDARD",
    "deviceId": 26431167,
}

config_best_practice_summary_1 = {
    "bestPracticeNuggetId": "IOS_XR_UNSUPP_TRANSEIVER",
    "bestPracticePrimaryTechnology": "*Network Management",
    "bestPracticeRisk": "Low",
    "bestPracticeRuleId": "11148",
    "bestPracticeSecondaryTechnology": "",
    "bestPracticeTitle": "System SNMP Traps Not Enabled",
    "softwareType": "NX-OS",
    "totalDeviceCount": 4,
}


def test_config_best_practice_rule_model() -> None:
    for config_best_practice_rule_dict in [config_best_practice_rule_1, config_best_practice_rule_2]:
        config_best_practice_rule = ConfigBestPracticeRule(**config_best_practice_rule_dict)
        check_model_creation(input_dict=config_best_practice_rule_dict, model_instance=config_best_practice_rule)


def test_config_best_practice_rule_reference() -> None:
    config_best_practice_rule_reference = ConfigBestPracticeRuleReference(**config_best_practice_rule_reference_1)
    check_model_creation(
        input_dict=config_best_practice_rule_reference_1, model_instance=config_best_practice_rule_reference
    )


def test_config_best_practice_detail() -> None:
    config_best_practice_detail = ConfigBestPracticeDetail(**config_best_practice_detail_1)
    check_model_creation(input_dict=config_best_practice_detail_1, model_instance=config_best_practice_detail)


def test_config_best_practice_summary() -> None:
    config_best_practice_summary = ConfigBestPracticeSummary(**config_best_practice_summary_1)
    check_model_creation(input_dict=config_best_practice_summary_1, model_instance=config_best_practice_summary)
