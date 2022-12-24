import requests
import json
import webbrowser

class Intramove:
    def __init__(self):
        self.products = {"headlines": "prod_N1vFZNiYNDhyM3"}
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        self.api_key = None

    def buy_package(self, product:str="headlines", quantity:int=1):
        assert product in self.products.keys(), f"Product has to be in {self.products.keys()}"
        payload = {"product_id":self.products[product], "quantity":quantity}
        response = requests.post(
            "http://0.0.0.0:8000/checkout", headers=self.headers, params=payload
        )
        url = response.json()["session_id"]["url"]
        webbrowser.open(url)


    def get_api_key(self, email:str, name:str):
        payload = {"email": email, "name":name}
        response = requests.get(
            "http://0.0.0.0:8000/client_key", headers=self.headers, params=payload
        )
        return (response.json())

    def analyze_headline(self, headline:str, date:str, api_key:str, callback_url):

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
            "http://0.0.0.0:8000/analyze/headline",
            headers=headline_headers,
            params=headline_payload,
        )
        return response.json()




    

