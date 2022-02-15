import logging
import requests
import jwt
import time

from typing import Optional, Dict, Generator
from .models import *


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def _get_all_items(url: str, headers: Dict[str, str], url_params: dict = None) -> Generator[dict, None, None]:
    """
    Function that will fetch all items
    :param url: str representing the url
    :param headers: dictionary containing the headers to be added to the request
    :param url_params: dictionary containing the url parameters
    :return: Generator
    """
    offset, total = None, None
    params = url_params if url_params is not None else {}
    while offset is None or offset <= total:
        if offset is not None:
            params['offset'] = offset
        try:
            resp = requests.session().get(url=url, headers=headers, params=params)
            resp.raise_for_status()
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as err:
            logger.error(
                f'Failed to get items: {err}'
            )
            raise err
        else:
            res = resp.json()
            offset = int(resp.headers.get('offset', 1)) + int(resp.headers.get('max', 0))
            total = int(resp.headers.get('total', 0))
            if 'items' in res:
                for item in res['items']:
                    yield item
            else:
                yield res


class BCSOIAPI:
    def __init__(self, client_id: str, client_secret: str, region: str, api_version: str = 'v2', server: str = 'api-cx.cisco.com') -> None:
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
        url = f'https://{self.server}/torii-auth/v1/token/'
        body = {
            "grantType": "client_credentials",
            "clientId": self.client_id,
            "secret": self.client_secret,
            "scope": "api.bcs.manage"
        }

        try:
            resp = requests.session().post(url=url, json=body)
            resp.raise_for_status()
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as err:
            logger.error(
                f'Failed to JSON Web Token(JWT): {err}'
            )
            raise err
        else:
            self.jwt = resp.json().get('accessToken')

    def _expiry_jwt(self) -> Optional[int]:
        """
        Helper function that decodes the JSON Web Token (JWT) when present and calculates how long it is still valid
        :return: integer representing the time in seconds the JWT is still valid, None when there is no JWT
        """
        if self.jwt is None:
            return None
        else:
            jwt_info = jwt.decode(self.jwt, options={'verify_signature': False})
            return time.time() - jwt_info['exp']

    def _check_and_renew_jwt(self) -> None:
        """
        Helper function that checks the expiry of the JSON Web Token (JWT) and when it is expired or is valid for
        less than 60 seconds will renew the token
        """
        jwt_validity = self._expiry_jwt()
        if jwt_validity is None or jwt_validity < 60:
            self._obtain_jwt()

    def get_items(self, model: BCSOIAPIBaseModel, url_params: dict = None) -> list:
        # check and renew JWT if needed
        self._check_and_renew_jwt()

        headers = {'Authorization': f'Bearer {self.jwt}'}
        url = f'https://{self.server}/bcs/staging/v2/{model.url_path()}'
        # url = f'https://{self.server}/{self.region}/bcs/{self.api_version}/{model.url_path()}'
        results = []
        for item in _get_all_items(url=url, headers=headers, url_params=url_params):
            results.append(model(**item))
        return results
    #
    #
    # def get_product_alerts_security_advisories(self, url_params: dict = None) -> List[SecurityAdvisory]:
    #     """
    #     Function that fetches all the Security Advisories and returns these as a list of SecurityAdvisory objects
    #     :param url_params: dictionary containing the url parameters
    #     :return: List containing SecurityAdvisory objects
    #     """
    #     # check and renew JWT if needed
    #     self._check_and_renew_jwt()
    #
    #     url = f'https://{self.server}/productAlerts/securityAdvisories'
    #     headers = {'Authorization': f'Bearer {self.jwt}'}
    #     results = []
    #     for item in _get_all_items(url=url, headers=headers, url_params=url_params):
    #         results.append(SecurityAdvisory(**item))
    #     return results
    #
    # def get_product_alerts_security_advisory_bulletins(self, url_params: dict = None) -> List[SecurityAdvisoryBulletin]:
    #     """
    #     Function that fetches all the PSIRT bulletins and returns these as a list of PsirtBulletin objects
    #     :param url_params: dictionary containing the url parameters
    #     :return: List containing PsirtBulletin objects
    #     """
    #     # check and renew JWT if needed
    #     self._check_and_renew_jwt()
    #
    #     url = f'https://{self.server}/productAlerts/securityAdvisoryBulletins'
    #     headers = {'Authorization': f'Bearer {self.jwt}'}
    #     results = []
    #     for item in _get_all_items(url=url, headers=headers, url_params=url_params):
    #         results.append(SecurityAdvisoryBulletin(**item))
    #     return results
    #
    # def get_devices(self, url_params: dict = None) -> List[Device]:
    #     # check and renew JWT if needed
    #     self._check_and_renew_jwt()
    #
    #     url = f'https://{self.server}/bcs/staging/v2/inventory/devices'
    #     headers = {'Authorization': f'Bearer {self.jwt}'}
    #     results = []
    #     for item in _get_all_items(url=url, headers=headers, url_params=url_params):
    #         results.append(Device(**item))
    #     return results
    #
    # def get_assets(self, url_params: dict = None) -> List[Asset]:
    #     return self._get_items(
    #         url=f'https://{self.server}/bcs/staging/v2/inventory/assets',
    #         url_params=url_params,
    #         model=Asset
    #     )
    #
    # def get_attributes(self, model: BCSOIAPIBaseMOdel) -> list:
    #     return self._get_items()
    #     model.url_path()
