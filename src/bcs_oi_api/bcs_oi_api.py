import logging
import time
from collections import defaultdict
from contextlib import closing
from typing import DefaultDict, Dict, Generator, List, Optional, Type

import jsonlines
import jwt
import requests

from .models import (
    BCSOIAPIBaseModel,
    ConfigBestPracticeRule,
    ConfigBestPracticeRuleReference,
    ConfigBestPracticeSummary,
    DeviceBulk,
    DeviceGroup,
    DeviceGroupMember,
    FieldNoticeBulletin,
    HardwareEndOfLifeBulletin,
    LastResetDetails,
    ResetCount,
    ResetHistory,
    RiskMitigationDetails,
    RiskMitigationSummary,
    SecurityAdvisoryBulletin,
    SoftwareEndOfLifeBulletin,
    SoftwareTrackMember,
    SoftwareTrackSoftwareMaintenanceUpgradeCompliance,
    SoftwareTrackSoftwareMaintenanceUpgradeRecommendation,
    SoftwareTrackSummary,
)

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


BULK_TYPE_MODEL_MAPPING = {
    "configuration_best_practice_rules": ConfigBestPracticeRule,
    "configuration_best_practice_rules_reference": ConfigBestPracticeRuleReference,
    "configuration_best_practice_summary": ConfigBestPracticeSummary,
    "device": DeviceBulk,
    "fn_bulletin": FieldNoticeBulletin,
    "groups": DeviceGroup,
    "group_members": DeviceGroupMember,
    "history_reset": ResetHistory,
    "lastest_reset": LastResetDetails,
    "hw_eox_bulletin": HardwareEndOfLifeBulletin,
    "psirt_bulletin": SecurityAdvisoryBulletin,
    "reset_count": ResetCount,
    "risk_mitigation_details": RiskMitigationDetails,
    "risk_mitigation_summary": RiskMitigationSummary,
    "sw_eox_bulletin": SoftwareEndOfLifeBulletin,
    "track_members": SoftwareTrackMember,
    "track_smupie_recommendation": SoftwareTrackSoftwareMaintenanceUpgradeRecommendation,
    "track_smupie_compliance": SoftwareTrackSoftwareMaintenanceUpgradeCompliance,
    "track_summary": SoftwareTrackSummary,
}


class BCSOIAPI:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        region: str,
        api_version: str = "v2",
        server: str = "api-cx.cisco.com",
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.server = server
        self.region = region
        self.api_version = api_version
        self.jwt = None

        self._obtain_jwt()

    def _obtain_jwt(self) -> None:
        """
        Helper function that will obtain a JSON Web Token (JWT) using the provided client id and client secret
        and storing this JWT
        """
        url = f"https://{self.server}/torii-auth/v1/token/"
        body = {
            "grantType": "client_credentials",
            "clientId": self.client_id,
            "secret": self.client_secret,
            "scope": "api.bcs.manage",
        }

        try:
            resp = requests.session().post(url=url, json=body)
            resp.raise_for_status()
        except (
            requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
        ) as err:
            logger.error(f"Failed to JSON Web Token(JWT): {err}")
            raise err
        else:
            self.jwt = resp.json().get("accessToken")

    def _expiry_jwt(self) -> Optional[int]:
        """
        Helper function that decodes the JSON Web Token (JWT) when present and calculates how long it is still valid
        :return: integer representing the time in seconds the JWT is still valid, None when there is no JWT
        """
        if self.jwt is None:
            return None
        else:
            jwt_info = jwt.decode(self.jwt, options={"verify_signature": False})
            return time.time() - jwt_info["exp"]

    def _check_and_renew_jwt(self) -> None:
        """
        Helper function that checks the expiry of the JSON Web Token (JWT) and when it is expired or is valid for
        less than 300 seconds will renew the token
        """
        jwt_validity = self._expiry_jwt()
        if jwt_validity is None or jwt_validity < 300:
            self._obtain_jwt()

    def _get_response(self, url: str, headers: dict, url_params: Optional[dict] = None) -> requests.models.Response:
        """
        Helper function that fetches the response for the given url
        :param url: str representing the url
        :param headers: dict containing the headers to send in the request
        :param url_params: dict containing the url parameters to send in the request
        :return: Response object returned by sending GET request to the specified url
        """
        url_params = url_params if url_params is not None else {}
        try:
            response = requests.session().get(url=url, headers=headers, params=url_params)
            response.raise_for_status()
        except requests.exceptions.ConnectionError as err:
            logger.error(f"Failed to get items: {err}")
            raise err
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 429:
                retry_after = int(err.response.headers.get("Retry-After"))
                logger.info(f"Rate limited, waiting {retry_after} seconds")
                time.sleep(retry_after)
                return self._get_response(url=url, headers=headers, url_params=url_params)
            if err.response.status_code == 401:
                self._check_and_renew_jwt()
                headers["Authorization"] = f"Bearer {self.jwt}"
                return self._get_response(url=url, headers=headers, url_params=url_params)
            logger.error(f"Failed to get items: {err}")
            raise err
        else:
            return response

    def _get_all_items(
        self, url: str, headers: Dict[str, str], url_params: Optional[dict] = None
    ) -> Generator[dict, None, None]:
        """
        Helper function that will fetch all items
        :param url: str representing the url
        :param headers: dictionary containing the headers to be added to the request
        :param url_params: dictionary containing the url parameters
        :return: Generator
        """
        offset, total = None, None
        params = url_params if url_params is not None else {}
        while offset is None or offset <= total:
            if offset is not None:
                params["offset"] = offset
            response = self._get_response(url=url, headers=headers, url_params=params)
            res = response.json()
            offset = int(response.headers.get("offset", 1)) + int(response.headers.get("max", 0))
            total = int(response.headers.get("total", 0))
            for item in res["items"]:
                yield item

    def get_output(
        self,
        model: Type[BCSOIAPIBaseModel],
        url_params: Optional[dict] = None,
        headers: Optional[dict] = None,
    ) -> Generator[BCSOIAPIBaseModel, None, None]:
        """
        Function that fetches the output of the BCS OI API for the given model
        :param model: BCSOIAPI model class for which the output has to be fetched
        :param url_params: dict containing the url parameters to be added to the request
        :param headers: dict containing the headers to be added to the request
        :return: A generator which yields instances of objects of the model given as input for API endpoints
        """
        # check and renew JWT if needed
        self._check_and_renew_jwt()

        # Add Authorization to the headers
        headers = headers if headers is not None else {}
        headers["Authorization"] = f"Bearer {self.jwt}"

        # Constructing the url
        url = f"https://{self.server}/{self.region}/bcs/{self.api_version}/{model.url_path()}"

        if model.response_items():
            for item in self._get_all_items(url=url, headers=headers, url_params=url_params):
                yield model(**item)
        else:
            response = self._get_response(url=url, headers=headers, url_params=url_params)
            yield model(**response.json())

    def get_bulk_alerts(self) -> DefaultDict[str, List[BCSOIAPIBaseModel]]:
        """
        Function that fetches the output of the bulk/alerts endpoint
        :return: dictionary with as keys the names of the models and as value a list of objects of this model
        """
        # check and renew JWT if needed
        self._check_and_renew_jwt()

        url = f"https://{self.server}/{self.region}/bcs/{self.api_version}/bulk/alerts"
        res = defaultdict(list)
        with closing(requests.get(url, headers={"Authorization": f"Bearer {self.jwt}"}, stream=True)) as r:
            reader = jsonlines.Reader(r.iter_lines())
            for doc in reader:
                res[BULK_TYPE_MODEL_MAPPING[doc["type"]].__name__].append(BULK_TYPE_MODEL_MAPPING[doc["type"]](**doc))
        return res
