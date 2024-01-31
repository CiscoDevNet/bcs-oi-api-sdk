from typing import List, Optional

from ..models import BCSOIAPIBaseModel



__all__ = ["PvaPolicies", "PvaDetails", "PvaVariations","PvaDetailsFilter","PvaVariationsFilter","PvapoliciesFilter"]

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


class PvaDetails(BCSOIAPIBaseModel): #naming formats
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
    subPolicy_type: str

    @classmethod
    def url_path(cls) -> str:
        return "policyVariationAnalysis/policyVariations"


class PvaDetailsFilter(BCSOIAPIBaseModel):
    policyName: Optional[List[int]]


class PvaVariationsFilter(BCSOIAPIBaseModel):
    policyType: Optional[List[int]]


class PvapoliciesFilter(BCSOIAPIBaseModel):
    policyType: Optional[List[str]]