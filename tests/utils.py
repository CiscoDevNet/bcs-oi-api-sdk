import re
from datetime import date, datetime
from src.bcs_oi_api import BCSOIAPIBaseModel


def check_model_creation(input_dict: dict, model_instance: BCSOIAPIBaseModel):
    for k, v in input_dict.items():
        attribute_name = re.sub(r'(?<!^)(?=[A-Z])', '_', k).lower()
        if type(model_instance.__getattribute__(attribute_name)) not in [date, datetime]:
            assert model_instance.__getattribute__(attribute_name) == v
