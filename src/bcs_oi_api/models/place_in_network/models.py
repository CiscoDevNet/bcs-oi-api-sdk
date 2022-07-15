from typing import Optional

from ..models import BCSOIAPIBaseModel

__all__ = ["PINDetails"]


class PINDetails(BCSOIAPIBaseModel):
    device_id: int
    device_name: str
    predicted_importance: str
    predicted_role: str

    @classmethod
    def url_path(cls) -> str:
        return "placeInNetwork/details"


class PINDetailsFilter(BCSOIAPIBaseModel):
    device_id: Optional[list]
    predicted_importance: Optional[list]
    predicted_role: Optional[list]
