from .bulk import DeviceBulk
from .collectors import Collector
from .config_best_practice import (
    ConfigBestPracticeDetail,
    ConfigBestPracticeRule,
    ConfigBestPracticeRuleReference,
    ConfigBestPracticeSummary,
)
from .contracts import BaseProduct, Contract, OrderableProductId
from .device_groups import DeviceGroup, DeviceGroupMember
from .device_reset import LastResetDetails, ResetCount, ResetDetails, ResetHistory
from .inventory import Asset, Device
from .models import BCSOIAPIBaseModel
from .product_alerts import (
    FieldNotice,
    FieldNoticeBulletin,
    HardwareEndOfLife,
    HardwareEndOfLifeBulletin,
    SecurityAdvisory,
    SecurityAdvisoryBulletin,
    SecurityAdvisoryOutcome,
    SoftwareAdvisoryAlert,
    SoftwareEndOfLife,
    SoftwareEndOfLifeBulletin,
)
from .risk_mitigation import RiskMitigationDetails, RiskMitigationSummary
from .software_track import (
    SoftwareTrackMember,
    SoftwareTrackSoftwareMaintenanceUpgradeCompliance,
    SoftwareTrackSoftwareMaintenanceUpgradeRecommendation,
    SoftwareTrackSummary,
)
from .syslog import Syslog
