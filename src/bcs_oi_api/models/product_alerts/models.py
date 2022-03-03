from datetime import date, datetime
from enum import Enum
from typing import Optional

from ..models import BCSOIAPIBaseModel

__all__ = [
    "SecurityAdvisoryOutcome",
    "FieldNotice",
    "FieldNoticeBulletin",
    "SecurityAdvisory",
    "SecurityAdvisoryBulletin",
    "HardwareEndOfLife",
    "HardwareEndOfLifeBulletin",
    "SoftwareAdvisoryAlert",
    "SoftwareEndOfLife",
    "SoftwareEndOfLifeBulletin",
]


class SecurityAdvisoryOutcome(Enum):
    VULNERABLE = "Vulnerable"
    NOT_VULNERABLE = "Not Vulnerable"
    POTENTIALLY_VULNERABLE = "Potentially Vulnerable"


class FieldNoticeBulletin(BCSOIAPIBaseModel):
    bulletin_first_published_timestamp: datetime
    bulletin_last_updated_timestamp: datetime
    bulletin_mapping_caveat: str
    bulletin_title: str
    bulletin_url: str
    field_notice_id: str
    field_notice_type: str
    problem_description: str

    @classmethod
    def url_path(cls) -> str:
        return "productAlerts/fieldNoticeBulletins"


class FieldNotice(BCSOIAPIBaseModel):
    device_id: int
    field_notice_id: str
    match_confidence: str
    match_confidence_reason: str
    physical_asset_id: int

    @classmethod
    def url_path(cls) -> str:
        return "productAlerts/fieldNotices"


class SecurityAdvisory(BCSOIAPIBaseModel):
    device_id: int
    match_confidence: SecurityAdvisoryOutcome
    match_confidence_reason: str
    security_advisory_cold_id: int

    @classmethod
    def url_path(cls) -> str:
        return "productAlerts/securityAdvisories"


class SecurityAdvisoryBulletin(BCSOIAPIBaseModel):
    bug_ids: str
    bulletin_first_published_timestamp: datetime
    bulletin_last_updated_timestamp: datetime
    bulletin_mapping_caveat: str
    bulletin_summary: str
    bulletin_title: str
    bulletin_url: str
    bulletin_version: str
    common_vulnerability_scoring_system_base_score: str
    common_vulnerability_scoring_system_temporal_score: str
    cve_ids: str
    security_advisory_cold_id: int
    security_advisory_id: str
    security_impact_rating: str

    @classmethod
    def url_path(cls) -> str:
        return "productAlerts/securityAdvisoryBulletins"


class HardwareEndOfLife(BCSOIAPIBaseModel):
    current_end_of_life_milestone: str
    current_end_of_life_milestone_date: date
    device_id: int
    device_name: str
    hardware_end_of_life_id: int
    next_end_of_life_milestone: str
    next_end_of_life_milestone_date: Optional[date]
    physical_asset_id: int
    physical_asset_type: str
    product_id: str

    @classmethod
    def url_path(cls) -> str:
        return "productAlerts/hardwareEndOfLife"


class HardwareEndOfLifeBulletin(BCSOIAPIBaseModel):
    bulletin_number: str
    bulletin_title: str
    bulletin_url: str
    end_of_life_announcement_date: date
    end_of_new_service_attachment_date: Optional[date]
    end_of_routine_failure_analysis_date: Optional[date]
    end_of_sale_date: date
    end_of_service_contract_renewal_date: Optional[date]
    end_of_software_maintenance_releases_date: Optional[date]
    end_of_vulnerability_security_support_date: Optional[date]
    hardware_end_of_life_id: int
    last_day_of_support_date: Optional[date]
    last_ship_date: Optional[date]
    product_id: str

    @classmethod
    def url_path(cls) -> str:
        return "productAlerts/hardwareEndOfLifeBulletins"


class SoftwareEndOfLife(BCSOIAPIBaseModel):
    device_id: int
    software_end_of_life_id: int
    current_end_of_life_milestone: str
    current_end_of_life_milestone_date: Optional[date]
    device_name: str
    next_end_of_life_milestone: str
    next_end_of_life_milestone_date: Optional[date]
    software_type: str
    software_version: str

    @classmethod
    def url_path(cls) -> str:
        return "productAlerts/softwareEndOfLife"


class SoftwareEndOfLifeBulletin(BCSOIAPIBaseModel):
    software_end_of_life_id: int
    bulletin_number: str
    bulletin_title: str
    bulletin_url: str
    end_of_life_announcement_date: date
    end_of_sale_date: Optional[date]
    end_of_software_maintenance_releases_date: Optional[date]
    end_of_vulnerability_security_support_date: Optional[date]
    last_day_of_support_date: Optional[date]
    software_maintenance_version: str
    software_major_version: str
    software_train: str
    software_type: str

    @classmethod
    def url_path(cls) -> str:
        return "productAlerts/softwareEndOfLifeBulletins"


class SoftwareAdvisoryAlert(BCSOIAPIBaseModel):
    device_id: int
    device_name: str
    image_name: str
    software_alert_type: str
    software_alert_url: str
    software_type: str
    software_version: str

    @classmethod
    def url_path(cls) -> str:
        return "productAlerts/softwareAdvisoryAlerts"
