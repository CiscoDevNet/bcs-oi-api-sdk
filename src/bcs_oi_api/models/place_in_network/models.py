from ..models import BCSOIAPIBaseModel


__all__ = ["Details"]


class Details(BCSOIAPIBaseModel):
    device_id: int
    device_name: str
    predicted_importance: str
    predicted_role: str

    @classmethod
    def url_path(cls) -> str:
        return "placeInNetwork/details"
