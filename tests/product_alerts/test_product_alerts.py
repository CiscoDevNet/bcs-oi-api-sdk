from src.bcs_oi_api.models import (
    FieldNotice,
    FieldNoticeBulletin,
    HardwareEndOfLife,
    HardwareEndOfLifeBulletin,
    SecurityAdvisory,
    SecurityAdvisoryBulletin,
    SoftwareAdvisoryAlert,
    SoftwareEndOfLife,
    SoftwareEndOfLifeBulletin,
)
from tests.utils import check_model_creation

field_notice_bulletin_1: dict = {
    "bulletinFirstPublishedTimestamp": "2006-03-02T00:00:00",
    "bulletinLastUpdatedTimestamp": "2007-02-22T09:52:07",
    "bulletinMappingCaveat": "Deviation numbers are not automatically checked.",
    "bulletinTitle": "FN# 62271 CRS-8: AC Power Supplies may encounter hang.",
    "bulletinUrl": "http://www.cisco.com/en/US/ts/fn/620/fn62271.html",
    "fieldNoticeId": "62271",
    "fieldNoticeType": "Hardware",
    "problemDescription": "CRS-8 AC Power Supplies occasionally lose communication capabilities due to an I2C hang. ",
}


def test_field_notice_bulletin_model() -> None:
    field_notice_bulletin = FieldNoticeBulletin(**field_notice_bulletin_1)
    check_model_creation(input_dict=field_notice_bulletin_1, model_instance=field_notice_bulletin)


field_notice_1: dict = {
    "deviceId": 24948009,
    "fieldNoticeId": "64156",
    "matchConfidence": "Not Vulnerable",
    "matchConfidenceReason": "No Match on Product Family ,SW Version; Match on SW Type ",
    "physicalAssetId": 256129731,
}


def test_field_notice_model() -> None:
    field_notice = FieldNotice(**field_notice_1)
    check_model_creation(input_dict=field_notice_1, model_instance=field_notice)


security_advisory_bulletin_1: dict = {
    "bugIds": "CSCek37177",
    "bulletinFirstPublishedTimestamp": "2007-01-24T00:00:00",
    "bulletinLastUpdatedTimestamp": "2007-01-24T00:00:00",
    "bulletinMappingCaveat": "",
    "bulletinSummary": "Cisco has released software updates that address these vulnerabilities. ",
    "bulletinTitle": "Crafted TCP Packet Can Cause Denial of Service",
    "bulletinUrl": "http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20070124-crafted-tcp",
    "bulletinVersion": "1.1",
    "commonVulnerabilityScoringSystemBaseScore": "3.3",
    "commonVulnerabilityScoringSystemTemporalScore": "2.7",
    "cveIds": "CVE-2007-0479",
    "securityAdvisoryColdId": 59,
    "securityAdvisoryId": "cisco-sa-20070124-crafted-tcp",
    "securityImpactRating": "Low",
}


def test_security_advisory_bulletin_model() -> None:
    security_advisor_bulletin = SecurityAdvisoryBulletin(**security_advisory_bulletin_1)
    check_model_creation(input_dict=security_advisory_bulletin_1, model_instance=security_advisor_bulletin)


security_advisory_1: dict = {
    "deviceId": 24932812,
    "matchConfidence": "Not Vulnerable",
    "matchConfidenceReason": "No Match on SW Version; Match on SW Type",
    "securityAdvisoryColdId": 134,
}


def test_security_advisory_model() -> None:
    security_advisory = SecurityAdvisory(**security_advisory_1)
    check_model_creation(input_dict=security_advisory_1, model_instance=security_advisory)


software_advisory_alert_1: dict = {
    "deviceId": 26431166,
    "deviceName": "10.81.98.8",
    "imageName": "C3560-IPSERVICESK9-M",
    "softwareAlertType": "SA",
    "softwareAlertUrl": "http://www.cisco.com/web/software/DefTracker/280805679/SA/ac104247.html",
    "softwareType": "IOS",
    "softwareVersion": "12.2(50)SE",
}


def test_software_advisory_alert_model() -> None:
    software_advisory_alert = SoftwareAdvisoryAlert(**software_advisory_alert_1)
    check_model_creation(input_dict=software_advisory_alert_1, model_instance=software_advisory_alert)


hardware_end_of_life_bulletin_1: dict = {
    "bulletinNumber": "EOL12308",
    "bulletinTitle": "Nexus 5500 Series Switches ",
    "bulletinUrl": "https://www.cisco.com/c/en/us/products/collateral/switches/",
    "endOfLifeAnnouncementDate": "2018-05-05",
    "endOfNewServiceAttachmentDate": "2020-05-04",
    "endOfRoutineFailureAnalysisDate": "2020-05-04",
    "endOfSaleDate": "2019-05-05",
    "endOfServiceContractRenewalDate": "2023-08-03",
    "endOfSoftwareMaintenanceReleasesDate": "2020-05-04",
    "endOfVulnerabilitySecuritySupportDate": "2022-05-04",
    "hardwareEndOfLifeId": 415556,
    "lastDayOfSupportDate": "2024-05-31",
    "lastShipDate": "2019-08-04",
    "productId": "N5K-C5548UP",
    "replacementProductId": "N5K-C5548UB",
}

hardware_end_of_life_bulletin_2: dict = {
    "bulletinNumber": "EOL12308",
    "bulletinTitle": "Nexus 5500 Series Switches ",
    "bulletinUrl": "https://www.cisco.com/c/en/us/products/collateral/switches/",
    "endOfLifeAnnouncementDate": "2018-05-05",
    "endOfNewServiceAttachmentDate": None,
    "endOfRoutineFailureAnalysisDate": None,
    "endOfSaleDate": "2019-05-05",
    "endOfServiceContractRenewalDate": None,
    "endOfSoftwareMaintenanceReleasesDate": None,
    "endOfVulnerabilitySecuritySupportDate": None,
    "hardwareEndOfLifeId": 415556,
    "lastDayOfSupportDate": None,
    "lastShipDate": None,
    "productId": "N5K-C5548UP",
    "replacementProductId": "N5K-C5548UB",
}


def test_hardware_end_of_life_bulletin_model() -> None:
    for hw_eol_bulletin_dict in [hardware_end_of_life_bulletin_1, hardware_end_of_life_bulletin_2]:
        hardware_end_of_life_bulletin = HardwareEndOfLifeBulletin(**hw_eol_bulletin_dict)
        check_model_creation(input_dict=hw_eol_bulletin_dict, model_instance=hardware_end_of_life_bulletin)


hardware_end_of_life_1: dict = {
    "currentEndOfLifeMilestone": "EoSWM,EoRFA",
    "currentEndOfLifeMilestoneDate": "2020-05-04",
    "deviceId": 26809025,
    "deviceName": "10.122.208.29",
    "hardwareEndOfLifeId": 415556,
    "nextEndOfLifeMilestone": "EoVSS",
    "nextEndOfLifeMilestoneDate": "2022-05-04",
    "physicalAssetId": 342519674,
    "physicalAssetType": "Chassis",
    "productId": "N5K-C5548UP",
    "replacementProductId": "N5K-C5548UB",
}

hardware_end_of_life_2: dict = {
    "currentEndOfLifeMilestone": "EoSWM,EoRFA",
    "currentEndOfLifeMilestoneDate": "2020-05-04",
    "deviceId": 26809025,
    "deviceName": "10.122.208.29",
    "hardwareEndOfLifeId": 415556,
    "nextEndOfLifeMilestone": "EoVSS",
    "nextEndOfLifeMilestoneDate": None,
    "physicalAssetId": 342519674,
    "physicalAssetType": "Chassis",
    "productId": "N5K-C5548UP",
    "replacementProductId": "",
}


def test_hardware_end_of_life_model() -> None:
    for hw_eol_dict in [hardware_end_of_life_1, hardware_end_of_life_2]:
        hardware_end_of_life = HardwareEndOfLife(**hw_eol_dict)
        check_model_creation(input_dict=hw_eol_dict, model_instance=hardware_end_of_life)


software_end_of_life_bulletin_1: dict = {
    "bulletinNumber": "EOL7004",
    "bulletinTitle": "Cisco IOS Software Release 12.2(50)SG",
    "bulletinUrl": "http://www.cisco.com/en/US/prod/collateral/switches/ps5718/ps4324/eol_c51_593690.html",
    "endOfLifeAnnouncementDate": "2010-03-22",
    "endOfSaleDate": "2010-09-20",
    "endOfSoftwareMaintenanceReleasesDate": "2011-08-30",
    "endOfVulnerabilitySecuritySupportDate": "2013-09-19",
    "lastDayOfSupportDate": "2015-09-30",
    "softwareEndOfLifeId": 216,
    "softwareMaintenanceVersion": "50",
    "softwareMajorVersion": "12.2",
    "softwareTrain": "SG",
    "softwareType": "IOS",
}

software_end_of_life_bulletin_2: dict = {
    "bulletinNumber": "EOL7004",
    "bulletinTitle": "Cisco IOS Software Release 12.2(50)SG",
    "bulletinUrl": "http://www.cisco.com/en/US/prod/collateral/switches/ps5718/ps4324/eol_c51_593690.html",
    "endOfLifeAnnouncementDate": "2010-03-22",
    "endOfSaleDate": None,
    "endOfSoftwareMaintenanceReleasesDate": None,
    "endOfVulnerabilitySecuritySupportDate": None,
    "lastDayOfSupportDate": None,
    "softwareEndOfLifeId": 216,
    "softwareMaintenanceVersion": "50",
    "softwareMajorVersion": "12.2",
    "softwareTrain": "SG",
    "softwareType": "IOS",
}


def test_software_end_of_life_bulletin_model() -> None:
    for sw_eol_bulletin_dict in [software_end_of_life_bulletin_1, software_end_of_life_bulletin_2]:
        software_end_of_life_bulletin = SoftwareEndOfLifeBulletin(**sw_eol_bulletin_dict)
        check_model_creation(input_dict=sw_eol_bulletin_dict, model_instance=software_end_of_life_bulletin)


software_end_of_life_1: dict = {
    "currentEndOfLifeMilestone": "Announced",
    "currentEndOfLifeMilestoneDate": "2021-09-01",
    "deviceId": 25691707,
    "deviceName": "10.122.109.133",
    "nextEndOfLifeMilestone": "EoSale",
    "nextEndOfLifeMilestoneDate": "2022-03-02",
    "softwareEndOfLifeId": 1152,
    "softwareType": "FXOS",
    "softwareVersion": "2.8.1.125",
}

software_end_of_life_2: dict = {
    "currentEndOfLifeMilestone": "Announced",
    "currentEndOfLifeMilestoneDate": None,
    "deviceId": 25691707,
    "deviceName": "10.122.109.133",
    "nextEndOfLifeMilestone": "EoSale",
    "nextEndOfLifeMilestoneDate": None,
    "softwareEndOfLifeId": 1152,
    "softwareType": "FXOS",
    "softwareVersion": "2.8.1.125",
}


def test_software_end_of_life_model() -> None:
    for sw_eol_dict in [software_end_of_life_1, software_end_of_life_2]:
        software_end_of_life = SoftwareEndOfLife(**sw_eol_dict)
        check_model_creation(input_dict=sw_eol_dict, model_instance=software_end_of_life)
