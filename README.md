# Intramove (Alpha Version)

A client for interacting with Intramove.ai API

Developed by Abdellatif Dalab 2022

##  How to get access

Purchasing Credits

```python
from intramove import Intramove

imove = Intramove()

print(imove.get_available_packages()) # Displays all the available product packages 

imove.buy_package(product="headlines-15", quantity=1) # Opens a web browsers with a stripe payment link 

```

Once purchase is done
```python
from intramove import Intramove

imove = Intramove()

# Using the same email and name from checkout, get your unique ID
my_id = imove.get_id(email="dan@gmail.com", name="dan")

# Use your unique ID to get your active API key
my_api_key = imove.get_api_key(my_id)

# Start using the API!
callback_url= "" # You can specify a call-back url - if not, results will be returned

analysis = imove.analyze_headline(
    api_key=my_api_key,
    headline="ECB Hikes Rates by 50bps, Signals Further Increases",
    date="12/15/2022",
    callback_url=callback_url,
)

if not callback_url:
    print(analysis)
```
How the output would look

```python
{"text":"ECB Hikes Rates by 50bps, Signals Further IncreasesEuro Area Interest ...",
"datetime":"12/15/2022",
"sign":"bear",
"indicator":"rate hikes",
"description":"rate hikes increased",
"score":-0.6049461960792542}
```
