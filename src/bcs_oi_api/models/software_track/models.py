from datetime import date
from typing import Optional

from ..models import BCSOIAPIBaseModel

__all__ = [
    "SoftwareTrackSummary",
    "SoftwareTrackMember",
    "SoftwareTrackSoftwareMaintenanceUpgradeCompliance",
    "SoftwareTrackSoftwareMaintenanceUpgradeRecommendation",
]


class SoftwareTrackSummary(BCSOIAPIBaseModel):
    software_type: str
    software_track_candidate_version: str
    software_track_comments: str
    software_track_compliant_device_count: int
    software_track_description: str
    software_track_id: int
    software_track_last_modified_date: date
    software_track_name: str
    software_track_non_compliant_device_count: int
    software_track_compliance_percent: float
    software_track_flexible_compliance_percent: float
    software_track_previous_1_package_installation_envelope_criteria: str
    software_track_previous_1_software_maintenance_update_criteria: str
    software_track_previous_2_package_installation_envelope_criteria: str
    software_track_previous_2_software_maintenance_update_criteria: str
    software_track_previous_compliant_device_count: int
    software_track_previous_version_1: str
    software_track_previous_version_2: str
    software_track_rating: str
    software_track_recommendation_date: Optional[date]
    software_track_software_maintenance_update_compliance_percent: Optional[float]
    software_track_standard_package_installation_envelope_criteria: str
    software_track_standard_software_maintenance_update_count: Optional[int]
    software_track_standard_software_maintenance_update_criteria: str
    software_track_standard_version: str
    software_track_status: str
    software_track_total_device_count: int
    software_track_total_version_count: int
    software_track_upgrade_reason: str

    @classmethod
    def url_path(cls) -> str:
        return "softwareTrack/summary"


class SoftwareTrackMember(BCSOIAPIBaseModel):
    device_id: int
    is_software_track_compliant: bool
    is_software_track_flexible_compliant: bool
    software_track_id: int
    software_track_name: str
    software_track_package_installation_envelope_compliance: str
    is_software_track_previous_compliant: bool
    software_track_software_maintenance_update_compliance: str
    software_track_software_maintenance_update_compliant_count: int
    software_track_software_maintenance_update_extra_count: int
    software_track_software_maintenance_update_missing_count: int
    software_track_standard_software_maintenance_update_count: Optional[int]

    @classmethod
    def url_path(cls) -> str:
        return "softwareTrack/members"


class SoftwareTrackSoftwareMaintenanceUpgradeCompliance(BCSOIAPIBaseModel):
    device_id: int
    software_maintenance_update_package_installation_envelope_type: str
    software_name: str
    software_role: str
    software_track_device_software_maintenance_update_PIE_action: str
    software_track_device_software_maintenance_update_PIE_compliance: str
    software_track_id: int
    software_track_name: str

    @classmethod
    def url_path(cls) -> str:
        return "softwareTrack/softwareMaintenanceUpgradeCompliance"


class SoftwareTrackSoftwareMaintenanceUpgradeRecommendation(BCSOIAPIBaseModel):
    software_name: str
    software_role: str
    software_track_id: int
    software_track_name: str
    software_track_recommendation_history: str

    @classmethod
    def url_path(cls) -> str:
        return "softwareTrack/softwareMaintenanceUpgradeRecommendations"
