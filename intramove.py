import requests
from bson import ObjectId
import webbrowser
from ratelimiter import RateLimiter



class Intramove:
    available_packages = ["headlines-15","headlines-500"]
    current_service_ip = "http://0.0.0.0:8000"
    @classmethod
    def get_available_packages(cls):
        return cls.available_packages

    def __init__(self):
        self.packages = {"headlines-15": "prod_N1vFZNiYNDhyM3"}
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        self.api_key = None
        self.client_ids = []

    def _call_endpoint(self, endpoint, payload):
        try:
            response = requests.get(
                f"{Intramove.current_service_ip}/{endpoint}", headers=self.headers, params=payload
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f'An HTTP error occurred: {err}')
        except requests.exceptions.RequestException as err:
            print(f'An error occurred while making the request: {err}')

        response = response.json()

        if not response: raise Exception("Client not registered.")

        return response

    def buy_package(self, product:str="headlines-15", quantity:int=1):
        assert product in self.packages.keys(), f"Product has to be in {self.packages.keys()}."
        assert quantity > 0, "Quantity has to be greater than 0."

        payload = {"product_id":self.packages[product], "quantity":quantity}
        response = requests.post(
            f"{Intramove.current_service_ip}/checkout", headers=self.headers, params=payload
        )
        url = response.json()["session_id"]["url"]
        webbrowser.open(url)
    
    @RateLimiter(max_calls=1, period=0.5)  
    def get_id(self, email:str, name:str):
        if not isinstance(email, str) or not email: 
            raise ValueError("email must be a non-empty string")
        if not isinstance(name, str) or not name:
            raise ValueError("name must be a non-empty string")

        payload = {"email": email, "name":name}
        response = self._call_endpoint("client_id", payload)
        return response

    @RateLimiter(max_calls=1, period=0.5)
    def get_api_key(self, client_id:str):
        if not isinstance(client_id, str) or not client_id:
            raise ValueError("client_id must be a non-empty string")

        try:
            ObjectId(client_id)
        except:
            raise Exception("Client ID doesn't have the right format, you must use the ID returned.")

        payload = {"client_id": client_id}

        self.api_key = self._call_endpoint("client_api_key", payload)
        return self.api_key

    @RateLimiter(max_calls=1, period=0.5)
    def credits_available(self, api_key:str):
        if not isinstance(api_key, str) or not api_key:
            raise ValueError("api_key must be a non-empty string")

        payload = {"api_key": api_key}
        return self._call_endpoint("credits_available", payload)
    
    @RateLimiter(max_calls=1, period=0.5)
    def credits_consumed(self, api_key:str):
        if not isinstance(api_key, str) or not api_key:
            raise ValueError("api_key must be a non-empty string")
        payload = {"api_key": api_key}
        return self._call_endpoint("credits_consumed", payload)

    @RateLimiter(max_calls=1, period=0.5)
    def status(self, api_key:str):
        if not isinstance(api_key, str) or not api_key:
            raise ValueError("api_key must be a non-empty string")
        payload = {"api_key": api_key}
        return self._call_endpoint("status", payload)

    @RateLimiter(max_calls=1, period=0.0001)
    def analyze_headline(self, headline:str, date:str, api_key:str, callback_url:str=""):

        if not isinstance(headline, str) or not headline:
            raise ValueError("headline must be a non-empty string")
        
        if not isinstance(date, str):
            raise ValueError("date must be a string")
        
        if not isinstance(api_key, str) or not api_key:
            raise ValueError("api_key must be a non-empty string")

        if not isinstance(callback_url, str):
            raise ValueError("callback_url must be a string")

        headline_payload = {
        "headline": headline,
        "date": date,
        "callback_url": callback_url,
        }

        headline_headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "api-key": api_key,
        }

        response = requests.post(
            f"{Intramove.current_service_ip}/analyze/headline",
            headers=headline_headers,
            params=headline_payload,
        )
        return response.json()




    

