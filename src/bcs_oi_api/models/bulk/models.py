from typing import List, Optional

from pydantic import validator

from ..config_best_practice import ConfigBestPracticeDetail
from ..contracts import Contract
from ..inventory import Asset, Device
from ..product_alerts import FieldNotice, HardwareEndOfLife, SecurityAdvisory, SoftwareEndOfLife


class AssetBulk(Asset):
    field_notices: List[FieldNotice]
    hardware_end_of_life: Optional[HardwareEndOfLife]
    contract: Optional[Contract]


class DeviceBulk(Device):
    assets: List[AssetBulk]
    configuration_best_practice: Optional[ConfigBestPracticeDetail]
    software_end_of_life: Optional[SoftwareEndOfLife]
    security_advisory: List[SecurityAdvisory]

    @validator("configuration_best_practice", pre=True)
    def check_configuration_best_practice(cls, v: dict) -> Optional[dict]:
        return v or None
