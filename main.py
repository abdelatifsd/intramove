from intramove import Intramove

imove = Intramove()

imove.buy_package(product="headlines", quantity=1)

api_key = imove.get_api_key(email="dan@gmail.com",name="dan")
analysis = imove.analyze_headline(api_key=api_key, headline="The US stock market crashed", date="12/12/2022", callback_url = "")
print(analysis)