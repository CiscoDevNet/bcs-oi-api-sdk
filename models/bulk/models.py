from typing import List, Optional, Union

from models.contracts import Contract
from models.inventory import Asset, Device
from models.config_best_practice import ConfigBestPracticeDetail
from models.product_alerts import FieldNotice, SoftwareEndOfLife, SecurityAdvisory, HardwareEndOfLife


class AssetBulk(Asset):
    field_notices: List[FieldNotice]
    hardware_end_of_life: Optional[HardwareEndOfLife]
    contract: Optional[Contract]


class DeviceBulk(Device):
    assets: List[AssetBulk]
    configuration_best_practice: Union[ConfigBestPracticeDetail, List[ConfigBestPracticeDetail]]
    software_end_of_life: Optional[SoftwareEndOfLife]
    security_advisory: List[SecurityAdvisory]
