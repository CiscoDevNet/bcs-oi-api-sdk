import re
from datetime import date, datetime

from src.bcs_oi_api import BCSOIAPIBaseModel
from src.bcs_oi_api.models import SecurityAdvisoryOutcome


def check_model_creation(input_dict: dict, model_instance: BCSOIAPIBaseModel) -> None:
    for k, v in input_dict.items():
        attribute_name = (re.sub(r"(?<!^)(?=[A-Z0-9])", "_", k).lower()).replace("p_i_e", "PIE")
        if isinstance(model_instance.__getattribute__(attribute_name), list):
            for i, j in enumerate(model_instance.__getattribute__(attribute_name)):
                check_model_creation(input_dict=v[i], model_instance=j)
        elif isinstance(model_instance.__getattribute__(attribute_name), BCSOIAPIBaseModel):
            check_model_creation(input_dict=v, model_instance=model_instance.__getattribute__(attribute_name))
        elif isinstance(model_instance.__getattribute__(attribute_name), SecurityAdvisoryOutcome):
            assert model_instance.__getattribute__(attribute_name).value == v
        elif isinstance(model_instance.__getattribute__(attribute_name), datetime):
            assert model_instance.__getattribute__(attribute_name) == datetime.strptime(v, "%Y-%m-%dT%H:%M:%S")
        elif isinstance(model_instance.__getattribute__(attribute_name), date):
            assert model_instance.__getattribute__(attribute_name) == datetime.strptime(v, "%Y-%m-%d").date()
        else:
            assert model_instance.__getattribute__(attribute_name) == v
