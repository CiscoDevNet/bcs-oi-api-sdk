from typing import List, Optional

from ..models import BCSOIAPIBaseModel

__all__ = ["PvaPolicies", "PvaDetails", "PvaVariations", "PvaDetailsFilter", "PvaVariationsFilter", "PvaPoliciesFilter"]


class PvaAppliedInterface(BCSOIAPIBaseModel):
    direction: str
    interface: str


class PvaPolicies(BCSOIAPIBaseModel):
    applied: int
    applied_interfaces: List[PvaAppliedInterface]
    device_id: int
    similarity_hash: str
    host_name: str
    policy_name: str
    policy_type: str
    product_family: str
    sub_policy_type: str

    @classmethod
    def url_path(cls) -> str:
        return "policyVariationAnalysis/devicesPolicies"


class PvaDetails(BCSOIAPIBaseModel):
    applied: int
    device_count: int
    policy_complexity: str
    policy_name: str
    policy_type: str
    product_family: str
    sub_policy_type: str
    policy_variations: int

    @classmethod
    def url_path(cls) -> str:
        return "policyVariationAnalysis/details"


class PvaVariations(BCSOIAPIBaseModel):
    is_primary_policy_variation: bool
    device_count: int
    similarity_hash: str
    policy_name: str
    policy_type: str
    product_family: str
    sub_policy_type: str

    @classmethod
    def url_path(cls) -> str:
        return "policyVariationAnalysis/policyVariations"


class PvaDetailsFilter(BCSOIAPIBaseModel):
    applied: Optional[int]
    policy_type: Optional[List[str]]
    policy_name: Optional[List[str]]
    policy_complexity: Optional[List[str]]


class PvaVariationsFilter(BCSOIAPIBaseModel):
    policy_type: Optional[List[str]]
    policy_name: Optional[List[str]]


class PvaPoliciesFilter(BCSOIAPIBaseModel):
    policy_type: Optional[List[str]]
    policy_name: Optional[List[str]]
