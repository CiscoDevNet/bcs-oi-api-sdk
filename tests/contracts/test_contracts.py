from datetime import datetime

from src.bcs_oi_api.models import BaseProduct, Contract, OrderableProductId

contract_1 = {
    "baseProductIdList": [{"baseProductId": "QSFP-100G-SM-SR="}],
    "contractSiteAddress": "225 W. TASMAN DRIVE",
    "contractSiteCity": "SAN JOSE",
    "contractSiteCountry": "US",
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
    "warrantyEndDate": "2020-11-15",
    "warrantyType": "WARR-1YR-LTD-HW",
    "warrantyTypeDescription": "http://www.cisco.com/go/warranty",
}


def test_contract_model():
    contract = Contract(**contract_1)
    assert contract.is_covered == contract_1["isCovered"]
    assert isinstance(contract.base_product_id_list[0], BaseProduct)
    assert contract.base_product_id_list[0].base_product_id == contract_1["baseProductIdList"][0]["baseProductId"]
    assert contract.warranty_end_date == datetime.strptime(contract_1["warrantyEndDate"], "%Y-%m-%d").date()
    assert isinstance(contract.orderable_product_id_list[0], OrderableProductId)
    assert (
        contract.orderable_product_id_list[0].item_position == contract_1["orderableProductIdList"][0]["itemPosition"]
    )
