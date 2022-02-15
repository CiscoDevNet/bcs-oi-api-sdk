from datetime import datetime

from models import (
    ConfigBestPracticeDetail,
    ConfigBestPracticeRule,
    ConfigBestPracticeRuleReference,
    ConfigBestPracticeSummary,
)

config_best_practice_rule_1 = {
    "bestPracticeCaveat": "",
    "bestPracticeCorrectiveAction": "In the global configuration mode,enter 'snmp-server enable traps system' "
    "command to enable system traps.",
    "bestPracticeDescription": "If NX-OS device has system configured and running and SNMP Traps enabled then flag an "
    "exception if globally you don't find:  \n\nsnmp-server enable traps system",
    "bestPracticeNuggetId": 550118,
    "bestPracticePrimaryTechnology": "*Network Management",
    "bestPracticeRecommendation": "Cisco recommends to enable SNMP traps,as they are helpful to log the event "
    "related to system process and can be used for troubleshooting when required.",
    "bestPracticeRisk": "Low",
    "bestPracticeRuleId": 11148,
    "bestPracticeSecondaryTechnology": "",
    "bestPracticeTitle": "System SNMP Traps Not Enabled",
    "createdTimestamp": "2016-06-04T04:01:00",
    "softwareType": "NX-OS",
    "bestPracticeRuleModificationTimestamp": None,
}

config_best_practice_rule_reference_1 = {
    "bestPracticeRuleId": 11148,
    "bestPracticeUrl": "http://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus7000/sw/system-management/"
    "command/reference/n7k_sm_cmd_ref/sm_cmd_s.html#pgfId-1035395",
    "bestPracticeUrlTitle": "Nexus 7000 System Command Reference",
}

config_best_practice_detail_1 = {
    "bestPracticeNuggetId": 550118,
    "bestPracticeRuleId": 11148,
    "configSource": "STANDARD",
    "deviceId": 26431167,
}

config_best_practice_summary_1 = {
    "bestPracticeNuggetId": 550118,
    "bestPracticePrimaryTechnology": "*Network Management",
    "bestPracticeRisk": "Low",
    "bestPracticeRuleId": 11148,
    "bestPracticeSecondaryTechnology": "",
    "bestPracticeTitle": "System SNMP Traps Not Enabled",
    "softwareType": "NX-OS",
    "totalDeviceCount": 4,
}


def test_config_best_practice_rule_model():
    config_best_practice_rule = ConfigBestPracticeRule(**config_best_practice_rule_1)
    assert (
        config_best_practice_rule.best_practice_rule_id
        == config_best_practice_rule_1["bestPracticeRuleId"]
    )
    assert config_best_practice_rule.best_practice_rule_modification_timestamp is None
    assert config_best_practice_rule.created_timestamp == datetime.strptime(
        config_best_practice_rule_1["createdTimestamp"], "%Y-%m-%dT%H:%M:%S"
    )


def test_config_best_practice_rule_reference():
    config_best_practice_rule_reference = ConfigBestPracticeRuleReference(
        **config_best_practice_rule_reference_1
    )
    assert (
        config_best_practice_rule_reference.best_practice_url_title
        == config_best_practice_rule_reference_1["bestPracticeUrlTitle"]
    )


def test_config_best_practice_detail():
    config_best_practice_detail = ConfigBestPracticeDetail(
        **config_best_practice_detail_1
    )
    assert (
        config_best_practice_detail.best_practice_nugget_id
        == config_best_practice_detail_1["bestPracticeNuggetId"]
    )


def test_config_best_practice_summary():
    config_best_practice_summary = ConfigBestPracticeSummary(
        **config_best_practice_summary_1
    )
    assert (
        config_best_practice_summary.total_device_count
        == config_best_practice_summary_1["totalDeviceCount"]
    )
