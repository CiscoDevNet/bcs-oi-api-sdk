from bcs_oi_api import BCSOIAPI
from bcs_oi_api.models import SISummary, SISummaryFilter, SIDetails, SIDetailsFilter

bcs_oi_api = BCSOIAPI(
    client_id='f526e3e4-ed5e-46f1-88f9-8358c463a80a',
    client_secret='mnzNzvY9fQOBGEMJkT3UliOXO7HRP0yc',
    region='us'
)
filter_params = {
    "threshold": [1]
}

filter_parameter = SISummaryFilter.parse_obj(filter_params)
# inventory_devices = bcs_oi_api.get_output(model=SISummary,filter_=filter_parameter)
# for inventory_device in inventory_devices:
#     print(inventory_device)
filter_parameter = SIDetailsFilter.parse_obj(filter_params)
inventory_devices = bcs_oi_api.get_output(model=SIDetails,filter_=filter_parameter)
for inventory_device in inventory_devices:
    print(inventory_device)