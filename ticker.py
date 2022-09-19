import requests as r 
from requests.exceptions import HTTPError


API_URL = "https://ed8boq.deta.dev/v1/overview/"


class Ticker:
    def __init__(self, tickername):
        self._tickername = tickername

    @property
    def ticker_data(self) -> dict:
        url = API_URL + self._tickername

        try:
            data = r.get(url)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
        except Exception as err:
            print(f'Other error occurred: {err}') 
        else:
            print('Success!')

        return data.json()

    @property
    def SMA200(self):
        return round(self.ticker_data.get("SMA200"),2)
    
    @property
    def SMA220(self):
        return round(self.ticker_data.get("SMA220"),2)

    @property
    def PRICE(self): 
        return round(self.ticker_data.get("current_course"),2)
    
    @property
    def sma200_CROSSED(self): 
        return self.ticker_data.get("is_sma200_cross")
    
    @property
    def sma220_CROSSED(self): 
        return self.ticker_data.get("is_sma220_cross")
    
