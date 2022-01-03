from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class PsirtOutcome(Enum):
    VULNERABLE = 'Vulnerable'
    NOT_VULNERABLE = 'Not Vulnerable'
    POTENTIALLY_VULNERABLE = 'Potentially Vulnerable'


def _to_camel(string: str) -> str:
    return f'{string.split("_")[0]}{"".join(word.capitalize() for word in string.split("_")[1:])}'


class PsirtResult(BaseModel):
    device_id: int
    match_confidence: PsirtOutcome
    match_confidence_reason: str
    psirt_cold_id: int

    class Config:
        alias_generator = _to_camel
        allow_population_by_field_name = True


class PsirtBulletin(BaseModel):
    bulletin_first_published: datetime
    bulletin_last_updated: datetime
    bulletin_mapping_caveat: str
    bulletin_summary: str
    bulletin_title: str
    bulletin_url: str
    bulletin_version: str
    cisco_bug_ids: str
    cve_id: str
    cvss_Base: str
    cvss_temporal: str
    psirt_advisory_id: str
    psirt_cold_id: int
    sir: str

    class Config:
        alias_generator = _to_camel
        allow_population_by_field_name = True
