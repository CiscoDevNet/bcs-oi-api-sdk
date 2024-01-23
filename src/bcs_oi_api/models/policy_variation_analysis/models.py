from typing import List, Optional

from ..models import BCSOIAPIBaseModel



__all__ = ["pvapolicies", "pvadetails", "pvaVariations","pvadetailsFilter","pvaVariationsFilter","pvapoliciesFilter"]


class pvapolicies(BCSOIAPIBaseModel):
    applied: dict
    direction: dict
    interface: str
    deviceId: int
    similarityHash: str
    hostName: str
    policyName: str
    policyType: str
    productFamily: str
    subPolicyType: str

    @classmethod
    def url_path(cls) -> str:
        return "policyVariationAnalysis/devicesPolicies"


class pvadetails(BCSOIAPIBaseModel): #naming formats
    applied: int
    deviceCount: int
    policyComplexity: str
    policyName: str
    policyType: str
    productFamily: str
    subPolicyType: str
    policyVariations: int

    @classmethod
    def url_path(cls) -> str:
        return "policyVariationAnalysis/details"


class pvaVariations(BCSOIAPIBaseModel):
    isPrimaryPolicyVariation: bool
    deviceCount: int
    similarityHash: str
    policyName: str
    policyType: str
    productFamily: str
    subPolicyType: str

    @classmethod
    def url_path(cls) -> str:
        return "policyVariationAnalysis/policyVariations"


class pvadetailsFilter(BCSOIAPIBaseModel):
    policyName: Optional[List[int]]


class pvaVariationsFilter(BCSOIAPIBaseModel):
    policyType: Optional[List[int]]


class pvapoliciesFilter(BCSOIAPIBaseModel):
    policyType: Optional[List[str]]
