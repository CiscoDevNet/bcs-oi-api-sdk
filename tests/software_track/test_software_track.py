from src.bcs_oi_api.models import SoftwareTrackSummary, SoftwareTrackMember, SoftwareTrackSoftwareMaintenanceUpgradeCompliance, SoftwareTrackSoftwareMaintenanceUpgradeRecommendation
from tests.utils import check_model_creation

sw_track_summary_1 = {
    "softwareType": "IOS XR",
    "softwareTrackCandidateVersion": "",
    "softwareTrackComments": "Created By Default on 14-OCT-17",
    "softwareTrackCompliantDeviceCount": 0,
    "softwareTrackDescription": "IOS XR",
    "softwareTrackId": 343768,
    "softwareTrackLastModifiedDate": "2019-04-15",
    "softwareTrackName": "IOS XR",
    "softwareTrackNonCompliantDeviceCount": 43,
    "softwareTrackCompliancePercent": 0.0,
    "softwareTrackFlexibleCompliancePercent": 0.0,
    "softwareTrackPrevious1PackageInstallationEnvelopeCriteria": "Ignore For Conformance",
    "softwareTrackPrevious1SoftwareMaintenanceUpdateCriteria": "Ignore For Conformance",
    "softwareTrackPrevious2PackageInstallationEnvelopeCriteria": "Require Exact Match",
    "softwareTrackPrevious2SoftwareMaintenanceUpdateCriteria": "Require Exact Match",
    "softwareTrackPreviousCompliantDeviceCount": 0,
    "softwareTrackPreviousVersion1": "",
    "softwareTrackPreviousVersion2": "",
    "softwareTrackRating": "Poor",
    "softwareTrackRecommendationDate": None,
    "softwareTrackSoftwareMaintenanceUpdateCompliancePercent": None,
    "softwareTrackStandardPackageInstallationEnvelopeCriteria": "Ignore For Conformance",
    "softwareTrackStandardSoftwareMaintenanceUpdateCount": None,
    "softwareTrackStandardSoftwareMaintenanceUpdateCriteria": "Ignore For Conformance",
    "softwareTrackStandardVersion": "6.1.3",
    "softwareTrackStatus": "Other",
    "softwareTrackTotalDeviceCount": 43,
    "softwareTrackTotalVersionCount": 24,
    "softwareTrackUpgradeReason": "Planned Maintenance"
}

sw_track_summary_2 = {
    "softwareType": "IOS XR",
    "softwareTrackCandidateVersion": "",
    "softwareTrackComments": "Created By Default on 14-OCT-17",
    "softwareTrackCompliantDeviceCount": 0,
    "softwareTrackDescription": "IOS XR",
    "softwareTrackId": 343768,
    "softwareTrackLastModifiedDate": "2019-04-15",
    "softwareTrackName": "IOS XR",
    "softwareTrackNonCompliantDeviceCount": 43,
    "softwareTrackCompliancePercent": 0.0,
    "softwareTrackFlexibleCompliancePercent": 0.0,
    "softwareTrackPrevious1PackageInstallationEnvelopeCriteria": "Ignore For Conformance",
    "softwareTrackPrevious1SoftwareMaintenanceUpdateCriteria": "Ignore For Conformance",
    "softwareTrackPrevious2PackageInstallationEnvelopeCriteria": "Require Exact Match",
    "softwareTrackPrevious2SoftwareMaintenanceUpdateCriteria": "Require Exact Match",
    "softwareTrackPreviousCompliantDeviceCount": 0,
    "softwareTrackPreviousVersion1": "",
    "softwareTrackPreviousVersion2": "",
    "softwareTrackRating": "Poor",
    "softwareTrackRecommendationDate": "2021-05-15",
    "softwareTrackSoftwareMaintenanceUpdateCompliancePercent": 90.2,
    "softwareTrackStandardPackageInstallationEnvelopeCriteria": "Ignore For Conformance",
    "softwareTrackStandardSoftwareMaintenanceUpdateCount": 10,
    "softwareTrackStandardSoftwareMaintenanceUpdateCriteria": "Ignore For Conformance",
    "softwareTrackStandardVersion": "6.1.3",
    "softwareTrackStatus": "Other",
    "softwareTrackTotalDeviceCount": 43,
    "softwareTrackTotalVersionCount": 24,
    "softwareTrackUpgradeReason": "Planned Maintenance"
}


def test_software_track_summary_model():
    for sw_track_summary_dict in [sw_track_summary_1, sw_track_summary_2]:
        software_track_summary = SoftwareTrackSummary(**sw_track_summary_dict)
        check_model_creation(input_dict=sw_track_summary_dict, model_instance=software_track_summary)


sw_track_member_1 = {
    "deviceId": 26364425,
    "isSoftwareTrackCompliant": False,
    "isSoftwareTrackFlexibleCompliant": False,
    "softwareTrackId": 254863,
    "softwareTrackName": "MDS 9100 Series Multilayer Fabric Switches",
    "softwareTrackPackageInstallationEnvelopeCompliance": "N/A - OS Version Non Conforming",
    "isSoftwareTrackPreviousCompliant": False,
    "softwareTrackSoftwareMaintenanceUpdateCompliance": "N/A - OS Version Non Conforming",
    "softwareTrackSoftwareMaintenanceUpdateCompliantCount": 0,
    "softwareTrackSoftwareMaintenanceUpdateExtraCount": 0,
    "softwareTrackSoftwareMaintenanceUpdateMissingCount": 0,
    "softwareTrackStandardSoftwareMaintenanceUpdateCount": None
}

sw_track_member_2 = {
    "deviceId": 26364425,
    "isSoftwareTrackCompliant": False,
    "isSoftwareTrackFlexibleCompliant": False,
    "softwareTrackId": 254863,
    "softwareTrackName": "MDS 9100 Series Multilayer Fabric Switches",
    "softwareTrackPackageInstallationEnvelopeCompliance": "N/A - OS Version Non Conforming",
    "isSoftwareTrackPreviousCompliant": False,
    "softwareTrackSoftwareMaintenanceUpdateCompliance": "N/A - OS Version Non Conforming",
    "softwareTrackSoftwareMaintenanceUpdateCompliantCount": 0,
    "softwareTrackSoftwareMaintenanceUpdateExtraCount": 0,
    "softwareTrackSoftwareMaintenanceUpdateMissingCount": 0,
    "softwareTrackStandardSoftwareMaintenanceUpdateCount": 9
}


def test_software_track_member_model():
    for sw_track_member_dict in [sw_track_member_1, sw_track_member_2]:
        software_track_member = SoftwareTrackMember(**sw_track_member_dict)
        check_model_creation(input_dict=sw_track_member_dict, model_instance=software_track_member)


sw_track_smu_compliance_1 = {
  "deviceId": 19811003,
  "softwareMaintenanceUpdatePackageInstallationEnvelopeType": "Committed",
  "softwareName": "ncs5500-isis-2.1.0.0-r652",
  "softwareRole": "PKG",
  "softwareTrackDeviceSoftwareMaintenanceUpdatePIEAction": "Add",
  "softwareTrackDeviceSoftwareMaintenanceUpdatePIECompliance": "Non-Compliant",
  "softwareTrackId": 343768,
  "softwareTrackName": "NCS5500"
}


def test_software_track_software_maintance_upgrade_compliance_model():
    software_track_software_maintenance_upgrade_compliance = SoftwareTrackSoftwareMaintenanceUpgradeCompliance(**sw_track_smu_compliance_1)
    check_model_creation(input_dict=sw_track_smu_compliance_1, model_instance=software_track_software_maintenance_upgrade_compliance)


sw_track_smu_recommendation_1 = {
    "softwareName": "ncs5500-fwding-3.0.0.1-r613.CSCvc64943",
    "softwareRole": "SMU",
    "softwareTrackId": 343768,
    "softwareTrackName": "IOS XR",
    "softwareTrackRecommendationHistory": "Previous1"
}


def test_software_track_software_maintenance_upgrade_recommendation_model():
    software_track_software_maintenance_upgrade_recommendation = SoftwareTrackSoftwareMaintenanceUpgradeRecommendation(**sw_track_smu_recommendation_1)
    check_model_creation(input_dict=sw_track_smu_recommendation_1, model_instance=software_track_software_maintenance_upgrade_recommendation)
