from src.bcs_oi_api.models import Contract
from tests.utils import check_model_creation

contract_1 = {
    "baseProductIdList": [{"baseProductId": "QSFP-100G-SM-SR="}],
    "contractSiteAddress": "225 W. TASMAN DRIVE",
    "contractSiteCity": "SAN JOSE",
    "contractSiteCountry": "US",
    "contractSiteShipDate": "2022-01-01 01:27:52",
    "contractSiteCustomerName": "CISCO SYSTEMS INC",
    "contractSiteStateProvince": "CA",
    "coveredProductLineEndDate": "2022-02-24",
    "isCovered": False,
    "orderableProductIdList": [
        {
            "itemDescription": "100GBASE CWDM4 Lite QSFP Transceiver, 2km over SMF, 10-60C",
            "itemPosition": "S",
            "itemType": "CARD",
            "orderableProductId": "QSFP-100G-SM-SR=",
            "pillarCode": "1,2",
        }
    ],
    "parentSerialNumber": "",
    "serialNumber": "INL23291758",
    "serviceContractNumber": "",
    "serviceLineDescription": "",
    "warrantyEndDate": "2020-11-15",
    "warrantyType": "WARR-1YR-LTD-HW",
    "warrantyTypeDescription": "http://www.cisco.com/go/warranty",
}


contract_2 = {
    "baseProductIdList": [{"baseProductId": "QSFP-100G-SM-SR="}],
    "contractSiteAddress": "225 W. TASMAN DRIVE",
    "contractSiteCity": "SAN JOSE",
    "contractSiteCountry": "US",
    "contractSiteShipDate": "2022-01-01 01:27:52",
    "contractSiteCustomerName": "CISCO SYSTEMS INC",
    "contractSiteStateProvince": "CA",
    "coveredProductLineEndDate": None,
    "isCovered": False,
    "orderableProductIdList": [
        {
            "itemDescription": "100GBASE CWDM4 Lite QSFP Transceiver, 2km over SMF, 10-60C",
            "itemPosition": "S",
            "itemType": "CARD",
            "orderableProductId": "QSFP-100G-SM-SR=",
            "pillarCode": "1,2",
        }
    ],
    "parentSerialNumber": "",
    "serialNumber": "INL23291758",
    "serviceContractNumber": "",
    "serviceLineDescription": "",
    "warrantyEndDate": None,
    "warrantyType": "WARR-1YR-LTD-HW",
    "warrantyTypeDescription": "http://www.cisco.com/go/warranty",
}


def test_contract_model() -> None:
    for contract_dict in [contract_1, contract_2]:
        contract = Contract(**contract_dict)
        check_model_creation(input_dict=contract_dict, model_instance=contract)
