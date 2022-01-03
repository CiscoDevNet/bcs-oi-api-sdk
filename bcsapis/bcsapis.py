import logging
import requests
import jwt
import time

from typing import Optional, List, Dict, Generator
from .models import PsirtResult, PsirtBulletin


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
    page, pages = None, None
    params = url_params if url_params is not None else {}
    while page is None or page <= pages:
        if page is not None:
            params['page'] = page
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
            page = res['page'] + 1
            pages = res['pages']
            for item in res['items']:
                yield item


class BCSApis:
    def __init__(self, client_id: str, client_secret: str, server: str = 'api-cx.cisco.com') -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.server = server
        self.jwt = None

        # self._obtain_jwt()

    def _obtain_jwt(self) -> None:
        """
        Helper function that will obtain a JSON Web Token (JWT) using the provided client id and client secret
        and storing this JWT
        """
        url = f'https://{self.server}/torii-auth/v1/token/{self.client_id}?' \
              f'claim=customer_id&claim=company_name&claim=cpyKey'
        headers = {
            'Authorization': self.client_secret
        }
        try:
            resp = requests.session().get(url=url, headers=headers)
            resp.raise_for_status()
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as err:
            logger.error(
                f'Failed to JSON Web Token(JWT): {err}'
            )
            raise err
        else:
            self.jwt = resp.text

    def _expiry_jwt(self) -> Optional[int]:
        """
        Helper function that decodes the JSON Web Token (JWT) when present and calculates how long it is still valid
        :return: integer representing the time in seconds the JWT is still valid, None when there is no JWT
        """
        if self.jwt is None:
            return None
        else:
            jwt_info = jwt.decode(self.token, options={'verify_signature': False})
            return time.time() - jwt_info['exp']

    def _check_and_renew_jwt(self) -> None:
        """
        Helper function that checks the expiry of the JSON Web Token (JWT) and when it is expired or is valid for
        less than 60 seconds will renew the token
        """
        jwt_validity = self._expiry_jwt()
        if jwt_validity is None or jwt_validity < 60:
            self._obtain_jwt()

    def get_product_alerts_psirt(self, url_params: dict = None) -> List[PsirtResult]:
        """
        Function that fetches all the PSIRT alerts and returns these as a list of PsirtResult objects
        :param url_params: dictionary containing the url parameters
        :return: List containing PsirtResult objects
        """
        # check and renew JWT if needed
        # self._check_and_renew_jwt()

        url = f'https://{self.server}/customer/280987866/productAlerts/psirt'
        # headers = {'Authorization': f'Bearer {self.jwt}'}
        headers = {'x-api-key': 'lqWTZbApQZgSR52ag8NS9jc5STobf6hMjm3Kyf30'}
        results = []
        for item in _get_all_items(url=url, headers=headers, url_params=url_params):
            results.append(PsirtResult(**item))
        return results

    def get_product_alerts_psirt_bulletins(self, url_params: dict = None) -> List[PsirtBulletin]:
        """
        Function that fetches all the PSIRT bulletins and returns these as a list of PsirtBulletin objects
        :param url_params: dictionary containing the url parameters
        :return: List containing PsirtBulletin objects
        """
        # check and renew JWT if needed
        # self._check_and_renew_jwt()

        url = f'https://{self.server}/customer/280987866/productAlerts/psirtBulletins'
        # headers = {'Authorization': f'Bearer {self.jwt}'}
        headers = {'x-api-key': 'lqWTZbApQZgSR52ag8NS9jc5STobf6hMjm3Kyf30'}
        results = []
        for item in _get_all_items(url=url, headers=headers, url_params=url_params):
            results.append(PsirtBulletin(**item))
        return results
