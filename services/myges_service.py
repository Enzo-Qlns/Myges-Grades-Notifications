from urllib.parse import urlparse, parse_qs
import requests
import http.client
import json

from config import Settings

config = Settings()


class MyGESService:
    def __init__(self) -> None:
        self._login = config.MYGES_LOGIN
        self._password = config.MYGES_PASSWORD
        self._client_id = "skolae-app"
        self._oauth_authorize_url = f"https://authentication.kordis.fr/oauth/authorize?client_id={self._client_id}&response_type=token"

    def get_access_token(self) -> str:
        response = requests.get(
            url=self._oauth_authorize_url,
            auth=(self._login, self._password),
            allow_redirects=False,
        )

        if response.status_code == 401:
            raise Exception("Wrong credentials")

        access_token = self.extract_access_token(response.headers)

        return access_token

    @staticmethod
    def extract_access_token(headers) -> str:
        location = headers.get("Location")

        if not location:
            raise Exception("Location header not found")

        location_url = urlparse(location)

        if not location_url.fragment:
            raise Exception("Impossible to extract fragment")

        query_params = parse_qs(location_url.fragment)
        access_token = query_params.get("access_token")

        if not access_token:
            raise Exception("Impossible to extract access token")

        return access_token[0]

    def get_grades(self, year: int) -> dict:
        access_token = self.get_access_token()

        conn = http.client.HTTPSConnection("api.kordis.fr")
        payload = ''
        headers = {
            "Authorization": f"Bearer {access_token}",
        }
        conn.request("GET", f"/me/{year}/grades", payload, headers)
        res = conn.getresponse()
        data = res.read().decode()
        return json.loads(data).get('result')


    # def get_grades(self, year: int) -> dict:
    #     conn = http.client.HTTPConnection("localhost:3000")
    #     conn.request("GET", f"/grades")
    #     res = conn.getresponse()
    #     data = res.read().decode()
    #     return json.loads(data)
