# Intramove (Alpha Version)

A client for interacting with Intramove.ai API

Developed by Abdellatif Dalab 2022

##  How to get access

Purchasing Credits

```python
from intramove.intramove import Intramove

imove = Intramove()

print(imove.get_available_packages()) # Displays all the available product packages 
# ["headlines-100","articles-100"]

# Opens a web browsers with a stripe payment link  - if it doesn't, you can simply run the link in a browser
# An account with your checkout email and name will be automatically registered in intramove's database
url, session_details = imove.buy_package(product="headlines-100", quantity=1) 
url, session_details = imove.buy_package(product="articles-100", quantity=1) 

```

Once purchase is done

```python
from intramove.intramove import Intramove

imove = Intramove()

# Using the same email and name from checkout, get your unique ID
my_id = imove.get_id(email="dan@gmail.com", name="dan")["client_id"]

# Use your unique ID to get your active API key
my_api_key = imove.get_api_key(my_id)["api_key"]

# Start using the API!
callback_url= "" # You can specify a call-back url - if not, results will be returned

headline_analysis = imove.analyze_headline(
    api_key=my_api_key,
    headline="ECB Hikes Rates by 50bps, Signals Further Increases",
    date="12/15/2022",
    callback_url=callback_url,
)

if not callback_url:
    print(headline_analysis)
```
How the headline analysis output would look
```python
# Headline analysis
{"text":"ECB Hikes Rates by 50bps, Signals Further IncreasesEuro Area Interest ...",
"datetime":"12/15/2022",
"sign":"bear",
"indicator":"rate hikes",
"description":"rate hikes increased",
"score":-0.6049461960792542}
```

```python
article = """The S&P/TSX Composite index extended early advances and closed 0.8% higher at 19,500 on Friday, notching a 0.3% increase on the week and outperforming its US counterparts with gains for energy producers and banks. In the meantime, investors digested domestic growth data, pointing to a stall in November and confirming that the Canadian economy expanded by 0.1% in October as growth in services-producing industries offset losses for goods-producing industries. Oil companies soared 4% to lead the gains in the session, tracking the second consecutive weekly increase for crude oil benchmarks. Toronto’s heavyweight banking and mining sectors also booked gains. On the other hand, concerns about tighter monetary policy continued to press the technology sector, leading losses for the day with a 3% slide for Shopify. The Toronto Exchange will be closed on Monday and Tuesday for holidays."""

article_analysis = imove.analyze_article(
    api_key=my_api_key,
    article=article,
    date="12/15/2022",
    callback_url=callback_url,
)

if not callback_url:
    print(article_analysis)
```
How the article analysis output would look
```python
{
    "chunks": [
        {
            "chunk": "pointing to a stall in November and confirming that the Canadian economy expanded by 0.1% in October as growth in services-producing industries offset losses for goods-producing industries.",
            "sign": "bull",
            "indicator": "gdp growth rate",
            "description": "gdp growth rate expanded",
            "score": 0.52849942445755,
        },
        {
            "chunk": "Oil companies soared 4% to lead the gains in the session",
            "sign": "bull",
            "indicator": "crude oil production",
            "description": "crude oil production climbed",
            "score": 0.5355966091156006,
        },
        {
            "chunk": "tracking the second consecutive weekly increase for crude oil benchmarks.",
            "sign": "bull",
            "indicator": "crude oil production",
            "description": "crude oil production climbed",
            "score": 0.6578888297080994,
        },
        {
            "chunk": "Toronto’s heavyweight banking and mining sectors also booked gains.",
            "sign": "bull",
            "indicator": "mining production",
            "description": "mining production booked gains",
            "score": 0.6116775274276733,
        },
    ],
    "average_score": 5.569899559020996,
    "average_sign": "bull",
    "datetime": "12/07/2022",
}
```
Other useful methods

```python
print(imove.status(my_api_key, product_name = "headlines-100")["status"]) # Prints whether the api key is active
print(imove.credits_consumed(my_api_key, product_name = "headlines-100")["credits_consumed"]) # Prints how many credits have been used
print(imove.credits_available(my_api_key, product_name = "headlines-100")["credits_available"]) # Prints how many credits are available

print(imove.status(my_api_key, product_name = "articles-100")["status"]) # Prints whether the api key is active
print(imove.credits_consumed(my_api_key, product_name = "articles-100")["credits_consumed"]) # Prints how many credits have been used
print(imove.credits_available(my_api_key, product_name = "articles-100")["credits_available"]) # Prints how many credits are available
```