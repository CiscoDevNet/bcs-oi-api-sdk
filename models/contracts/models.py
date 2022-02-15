from datetime import date
from typing import List, Optional

from ..models import BCSOIAPIBaseModel

__all__ = ["Contract"]


class BaseProduct(BCSOIAPIBaseModel):
    base_product_id: str


class OrderableProductId(BCSOIAPIBaseModel):
    item_description: str
    item_position: str
    item_type: str
    orderable_product_id: str
    pillar_code: str


class Contract(BCSOIAPIBaseModel):
    base_product_id_list: List[BaseProduct]
    contract_site_address: str
    contract_site_city: str
    contract_site_country: str
    contract_site_customer_name: str
    contract_site_state_province: str
    covered_product_line_end_date: Optional[date]
    is_covered: bool
    orderable_product_id_list: List[OrderableProductId]
    parent_serial_number: str
    serial_number: str
    service_contract_number: str
    service_line_description: str
    warranty_end_date: Optional[date]
    warranty_type: str
    warranty_type_description: str

    @classmethod
    def url_path(cls):
        return "contract/serials"
