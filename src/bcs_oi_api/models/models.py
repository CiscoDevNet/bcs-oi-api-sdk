from pydantic import BaseModel


def _to_camel(string: str) -> str:
    return f'{string.split("_")[0]}{"".join(word[0].upper()+word[1:] for word in string.split("_")[1:])}'


class BCSOIAPIBaseModel(BaseModel):
    class Config:
        alias_generator = _to_camel
        allow_population_by_field_name = True

    @classmethod
    def url_path(cls) -> str:
        return ""

    @classmethod
    def response_items(cls) -> bool:
        return True
